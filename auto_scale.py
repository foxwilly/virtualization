#!usr/bien/env python3
import time
import os
import subprocess
import random
def monitorCPU():
    Max_size = 4
    instance_number=0

    #keys need to be configured to avoid give the password
    #cpu = subprocess.run(("ssh", "cirros@172.24.4.63", "./cpu.sh"))
    cpu = random.randint(0,20)
    while True:
        print('the current cpu is:{0} '.format(cpu))
        if(cpu>20):
            print("deploy vm")
            #cli command to deploy the instnace
            openstack_command="openstack server create --flavor 1 --image f36a1548-66f4-4434-90d7-da784bb1bc18 --key-name test --security-group 9b072618-a486-484e-b719-1779033a9090 --nic net-id=05650c3e-e586-4502-acc1-e1fcde3f48e2 myNewInstance2"
            subprocess.run([openstack_command], shell=True)
            instance_number=instance_number+1
        else:
            print("everything is good, still watching...")
            #Evaluation period: 40 (this value denotes the time period in seconds for monitoring CPU usage)
            time.sleep(40)
        # exit condition:
        # Max size = 4 (this value denotes the maximum number of instances that should be spun)
        if (instance_number==Max_size):
            break

if __name__ == '__main__':
    monitorCPU()
