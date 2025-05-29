# Tenda CP3 reverse engineering

Around 1.5 years ago I decided to kick off my reverse-engineering journey with IoT devices. So, today I'd like to shed some light on my experience and results in the exploring security gaps of Chinese IP camera Tenda CP3.

What do I mean by reverse engineering of IoT devices?
First of all:
1) Device teardown and components identification
2) Dump of the firmware
3) Firmware analysis and vulnerabilities identification

During few programs analysis, I was lucky to found one vulnerability/backdoor which enabled me to carry out remote code execution attack and gain root access from the remote host.
Let's dive into it.

