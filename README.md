# Tenda CP3 reverse engineering

Around 1.5 years ago I decided to kick off my reverse-engineering journey with IoT devices. So, today I'd like to shed some light on my experience and results in the exploring security gaps of Chinese IP camera Tenda CP3.

What do I mean by reverse engineering of IoT devices?
First of all:
1) Device teardown and components identification
2) Dump of the firmware
3) Firmware analysis and vulnerabilities identification

During few programs analysis, I was lucky to found one vulnerability/backdoor which enabled me to carry out remote code execution attack and gain root access from the remote host.
Let's dive into it.


## Chapter 1: Camera teardown and components identification

Most likely, this is the easiest stage of the whole project since all you need is a solid screwdriver and 15 minutes of your free time. The are special internal engines which control the movement of the camera - thanks to it you can control the device remotely using the iOS/Android mobile app. After disabling few engines which are responsible for camera movement (you can control our camera from the iOS/Android app), the PCB from the camera is removed (Once all these engines are disabled, we take the PCB out and see the 'core' aka the brain of the device. In order to identify main elements with the best precision, I used the digital microscope. So, there are two main elements on PCB that need to be highlighted:

1) SoC of Tenda CP3 camera – _**Fulhan FH8626**_. This SoC is widely used in IP cameras and is responsible for image signal processing:
<img src="./assets/images/fulhan_microskope.jpg">

2) Flash chip – _**cFeon QH64A**_. This is the chip where the main camera firmware is located:
<img src="./assets/images/cfeon_microskope.jpg">

One crucial note here: I managed to find UART pins on the PCB right away, and they were even signed. Therefore, I didn’t need to identify them manually with help of multimeter (which isn't a rocket science though, but anyway). After soldering some wires to the UART pins, I connected them to the well-known hacking multi-tool called Bus Pirate. At this stage, I used Bus Pirate as USB-UART converter:
<img src="./assets/images/uart_buspirate.jpg">

I used minicom in order to establish serial connection with the camera, plugged device and saw uboot/linux kernel logs immediately. I tried to type some sh1t from the keyboard but camera demanded login/password from me (which is quite obvious). In such a situation, we could try to find some credentials in the network, but we are hackers, aren't we? Let’s do it in a hacker way and dump firmware in order to get access to file system where root credentials are located!

## Chapter 2: Firmware dump

In order to have some access to the file system of camera, we need to dump whole firmware from flash-chip. So I used Bus Pirate again but in a slightly different configuration: I connected SPI-clip to the flash chip and according to the cFeon chip scheme, I connected SPI-clip to the Bus Pirate. Here is what it looks like:
<img src="./assets/images/spi_buspirate.jpg">

Let's use the flashrom utility to dump the firmware:

```
sudo flashrom -p buspirate_spi:dev=/dev/ttyUSB0 -r camera_fw.bin
```
