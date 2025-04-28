import sys
import os
import psutil

# This program displays CPU and memory information using the psutil library.

# Function to fetch and display memory information
def get_memory_info():
    # Print total memory available in GB
    print("total_memory: " + str(psutil.virtual_memory().total / (1024.0 ** 3)))
    # Print available memory in GB
    print("available_memory: " + str(psutil.virtual_memory().available / (1024.0 ** 3)))
    # Print used memory in GB
    print("used_memory: " + str(psutil.virtual_memory().used / (1024.0 ** 3)))
    # Print memory usage percentage
    print("memory_percentage: " + str(psutil.virtual_memory().percent))

# Function to fetch and display CPU information
def get_cpu_info():
    # Print the number of physical cores
    print("physical_cores: " + str(psutil.cpu_count(logical=False)))
    # Print the total number of logical cores
    print("total_cores: " + str(psutil.cpu_count(logical=True)))
    # Print the current processor speed in MHz
    print("processor_speed: " + str(psutil.cpu_freq().current))
    # Print the CPU usage percentage for each core
    print("cpu_usage_per_core: " + str(dict(enumerate(psutil.cpu_percent(percpu=True, interval=1)))))
    # Print the total CPU usage percentage
    print("total_cpu_usage: " + str(psutil.cpu_percent(interval=1)))

# Main function to execute the program
def main() -> int:
    print("Starting Program")
    print("=============================")

    # Fetch and display memory information
    get_memory_info()
    # Fetch and display CPU information
    get_cpu_info()

# Entry point of the program
if __name__ == '__main__':
    sys.exit(main()) 
