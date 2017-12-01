#!/usr/bin/python
import os
import subprocess
import time


def check_status():
    while True:
        vpn_status = subprocess.check_output(['ipsec status'], shell=True, stderr=subprocess.STDOUT)
        vpn_status = str(vpn_status)
        vpn_status = vpn_status.split()
        vpn_status = vpn_status[7]
        if vpn_status == 'ESTABLISHED':
            print('matches')
            time.sleep(60)
        else:
            print('needs a restart')
            subprocess.check_output(['ipsec restart'], shell=True)


check_status()
