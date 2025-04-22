import sys
import threading

# Utility function to print blank lines
def printBlankLines(lines: int):
    for i in range(lines):
        print("")

def printMsg1(num):
    threading.get_ident()
    for thread in threading.enumerate(): 
       print(thread.name)
    print("Thread 1 cubed: {}" .format(num * num * num))


def printMsg2(num):
    threading.get_ident()
    for thread in threading.enumerate(): 
       print(thread.name)
    print("Thread 2 squared: {}" .format(num * num))

def showThreadingExample() -> None:
    print("Demonstrating Threading")
    t1 = threading.Thread(target=printMsg1, args=(10,))
    t2 = threading.Thread(target=printMsg2, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done With Threading!")



def main() -> int:
    print("Starting Program")
    print("=============================")

    showThreadingExample()


if __name__ == '__main__':
    sys.exit(main()) 
