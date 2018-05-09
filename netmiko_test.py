#Import modules

from netmiko import ConnectHandler


def connect_to_device(hostname):
     '''Takes a hostname as its single
        argumentand establishes a connection
        with that hostname
        ex. connect_to_device(router1)'''

     message = "Connecting to device"
     print_logger(message, hostname)
     net_d = ConnectHandler(host=hostname, username='ntc', password='ntc123', device_type='juniper_junos'


def deploy_commands(device, hostname, config_file):
    '''Takes 3 arguments: device, hostname, config_file
       where config_file is a file with a set of commands to run'''

    print("Sending commands from file | {}".format(hostname))
    device.send_config_from_file(config_file)

def print_logger(message,hostname):
    print("{} | {}".format(message, hostname))

def main():
    devices = ['vmx7', 'vmx8', 'vmx9']
    config_file = './configs/snmp.cfg'

    for device in devices:
        net_device = connect_to_device(device)
        deploy_commands(net_device, device, config_file)
        print_logger("Disconnecting fromdevice", device)
        net_device.disconnect()



if __name__ == "__main__":
    main()
