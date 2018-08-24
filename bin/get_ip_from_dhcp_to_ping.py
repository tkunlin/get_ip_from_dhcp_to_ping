#!//usr/bin/python3
# Description: This script can get the Mac address and IP address from DHCP server in Linux OS.
#              And try to ping those IP address, to ensure device is alive. 
#
# Author: Richard Tsai
# Date: 2018-05-29
#

import subprocess


DNSMASQ_FILE_PATH='/var/lib/misc/dnsmasq.leases'
WHITELIST_FILE_PATH='../conf/whitelist.txt'

def main():
   
    # Get the device IP address and Mac address from /var/lib/mis/dnsmasw.leases 
    
    with open(DNSMASQ_FILE_PATH) as file1:
        for line in file1:
            fields = line.strip().split()
            print('Device IP : ' +  fields[2]  + '    Device Mac Address : ' + fields[1])

            # Get the IP address from  white list 
            with open(WHITELIST_FILE_PATH) as file2:
               for line in file2:
                   mac  = line.strip().split()
                   print('Mac from white list: ' + mac[0])

                   ret=subprocess.call('ping -c 3 %s' % fields[2], shell=True, stdout=open('/dev/null','w'), stderr=subprocess.STDOUT)

                   if fields[1] == mac[0]  and ret ==0: 
                       print('%s is connected!' % fields[1])
                   elif fields[1] == mac[0] and ret ==1:
                       print('%s is disconnected!' % fields[1])
                   
   
                   if ret == 0:
                       print('%s is alive!' % fields[2])
                   else:
                       print('%s is down...' % fields[2])
 

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        pass