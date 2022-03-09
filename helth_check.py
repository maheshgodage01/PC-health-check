import shutil
import psutil
import socket
import os

def check_reboot():
    '''returns true if restart avaialabe false otherwise'''
    return os.path.exists('/run/reboot-required')

def disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free > 20

def cpu_usage():
    cu = psutil.cpu_percent(1)
    return cu < 70

def no_network():
    '''return true if  network is not available false otherwise'''
    try:
        socket.gethostbyname('www.googke.com')
        return False
    except:
        return True

if disk_usage("/") and cpu_usage():
    print("Disk and CPU usage is ok!!")
else:
    print("High Resource Using!")


if no_network():
    print("Network is Available")
else:
    print("Network is not available")
if check_reboot():
    print("reboot is avaialable...")
else:
    print("no any reboot is available...")
print("Finished...")
