#This is a script that will connect to a device and backup the config
#We can also add a check that will see if the file is older that a time we provide and create the backup

import os
import time
import subprocess
from netmiko import ConnectHandler

host7 = 'vmx7'
host8 = 'vmx8'
platform = 'juniper_junos'
username = 'ntc'
password = 'ntc123'


#Check if directory exists before creating
if not os.path.exists('./configs'):
    os.mkdir('./configs')

hosts = [host7, host8]


def save_config():
    for host in hosts:
        print('Connecting to {}'.format(host))
        session = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        time.sleep(2)
        print('Saving the configuration')
        vmx_config = session.send_command('show configuration', 'show configuration|display set')
        time.sleep(2)
        print('Backing up configuration for {}'.format(host))
        write_config = open('/home/ntc/files/configs/{}_config'.format(host), 'a')
        write_config.write('{}_config'.format(host))
        write_config.close()
        time.sleep(2)
        print('-' * 5)
        print('closing session with {}'.format(host))
        session.disconnect()



save_config()


time.sleep(2)

os.chdir('./configs')
print('Files can be located at:\n')

current_dir = os.getcwd()
print(current_dir)


file_location = subprocess.call('ls -lah | grep vmx ', shell=True)

print(file_location)

#Original
#print('Connecting to ' + hosts[0])
#vmx7_session = ConnectHandler(device_type=platform, ip=host7, username=username, password=password)
#
#time.sleep(2)
#print('Saving the configuration')
#vmx7_config = vmx7_session.send_command('show configuration', 'show configuration|display set')
#
#time.sleep(2)
#
#print('Backing up configuration for ' + hosts[0])
#write_7config = open('/home/ntc/files/configs/vmx7_config', 'a')
#write_7config.write(vmx7_config)
#write_7config.close()
#
#time.sleep(2)
#
#print('closing session with ' + hosts[0])
#vmx7_session.disconnect()
#
#
#print('=' * 5)
#
#print('Connecting to ' + hosts[1])
#vmx8_session = ConnectHandler(device_type=platform, ip=host8, username=username, password=password)
#
#time.sleep(2)
#print('Saving the configuration')
#vmx8_config = vmx8_session.send_command('show configuration', 'show configuration|display set')
#
#time.sleep(2)
#
#print('Backing up configuration for ' + hosts[1])
#write_8config = open('/home/ntc/files/configs/vmx8_config', 'a')
#write_8config.write(vmx8_config)
#write_8config.close()
#
#
#print('closing session with ' + hosts[1])
#vmx8_session.disconnect()
#
#
#time.sleep(2)
#
#os.chdir('./configs')
#print('Files can be located at:\n')
#current_dir = os.getcwd()
#print(current_dir)
#
#
#file_location = subprocess.call('ls -lah | grep vmx ', shell=True)
#
#print(file_location)
#
