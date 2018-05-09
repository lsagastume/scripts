
import subprocess
import os


def get_oobs():
    '''This send a command to shell and pulls oobs from devices.csv and saves it to ~/oob_hosts '''
    subprocess.call("awk -F, '/^oob/ {print $1}' /oc/local/netinfo/etc/devices.csv |grep -v ' - '|grep -v 'decom' > ~/oob_hosts", shell=True)

def get_cores():
    '''This send a command to shell and pulls cores from devices.csv and saves it to ~/core_hosts '''
    subprocess.call("awk -F, '/^core/ {print $1}' /oc/local/netinfo/etc/devices.csv |grep -v ' - '|grep -v 'decom' > ~/core_hosts", shell=True)


get_oobs()

#Save original working directory
orig_dir = os.getcwd()
home_dir = os.getenv('HOME')

#Since host files are saved in ~, I am changing to that directory before opening the file.
os.chdir(home_dir)

#open oob_hosts file to get oob names
with open('./oob_hosts', 'r') as oobs:
    oob_init = oobs.read()
oobs.closed

#splits oobs at line break and creates list
oob_list = oob_init.split('\n')

def ping_oob(devices):
    for device in devices:
        print("Testing {} reachability".format(device))
        results = os.system("ping {} -c 4".format(device))
        print(results)
        print('-' * 5)

ping_oob(oob_list)
