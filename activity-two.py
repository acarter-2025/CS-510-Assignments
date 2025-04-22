import sys
import psutil
import json

def get_process_info():
    process_info = []
    for process in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
        try:
            process_info.append({
                "pid": process.info['pid'],
                "name": process.info['name'],
                "memory_percent": process.info['memory_percent'],
                "cpu_percent": process.info['cpu_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print(json.dumps(process_info, indent=4))


def main() -> int:
    print("Starting Program")
    print("=============================")

    get_process_info()


if __name__ == '__main__':
    sys.exit(main())  
