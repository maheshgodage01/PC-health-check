import shutil
import psutil

def disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free > 20

def cpu_usage():
    cu = psutil.cpu_percent(1)
    return cu < 70

if disk_usage("/") and cpu_usage():
    print("Everything is OK!")
else:
    print("High Resource Using!")
