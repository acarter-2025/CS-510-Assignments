import sys
import os
import psutil

# Example program for Module 4
def get_memory_info():

    print("total_memory: " + str(psutil.virtual_memory().total / (1024.0 ** 3)))
    print("available_memory: " + str(psutil.virtual_memory().available / (1024.0 ** 3)))
    print("used_memory: " + str(psutil.virtual_memory().used / (1024.0 ** 3)))
    print("memory_percentage: " + str(psutil.virtual_memory().percent))

def get_cpu_info():
    print("physical_cores: " + str(psutil.cpu_count(logical=False)))
    print("total_cores: " + str(psutil.cpu_count(logical=True)))
    print("processor_speed: " + str(psutil.cpu_freq().current))
    print( "cpu_usage_per_core: " + str(dict(enumerate(psutil.cpu_percent(percpu=True, interval=1)))))
    print("total_cpu_usage: " + str(psutil.cpu_percent(interval=1)))


def main() -> int:
    print("Starting Program")
    print("=============================")

    get_memory_info(),
    get_cpu_info(),


if __name__ == '__main__':
    sys.exit(main()) 
