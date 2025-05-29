# Tenda CP3 reverse engineering

Around 1.5 years ago I decided to kick off my reverse-engineering journey with IoT devices. So, today I'd like to shed some light on my experience and results in the exploring security gaps of Chinese IP camera Tenda CP3.

What do I mean by reverse engineering of IoT devices?
First of all:
1) Device teardown and components identification
2) Dump of the firmware
3) Firmware analysis and vulnerabilities identification

During few programs analysis, I was lucky to found one vulnerability/backdoor which enabled me to carry out remote code execution attack and gain root access from the remote host.
Let's dive into it.


### Chapter 1: Camera teardown and components identification

Most likely, this is the easiest stage of the whole project since all you need is a solid screwdriver and 15 minutes of your free time. The are special internal engines which control the movement of the camera - thanks to it you can control the device remotely using the iOS/Android mobile app. After disabling few engines which are responsible for camera movement (you can control our camera from the iOS/Android app), the PCB from the camera is removed (Once all these engines are disabled, we take the PCB out and see the 'core' aka the brain of the device. In order to identify main elements with the best precision, I used the digital microscope. So, there are two main elements on PCB that need to be highlighted:

1) SoC of Tenda CP3 camera – _**Fulhan FH8626**_. This SoC is widely used in IP cameras and is responsible for image signal processing:
<img src="./assets/images/fulhan_microskope.jpg">
