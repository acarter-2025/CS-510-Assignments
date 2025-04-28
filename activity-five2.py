from threading import Semaphore, Thread
import time

# Initialize a semaphore with a maximum count of 3
# This limits the maximum number of threads that can run concurrently
semaphore = Semaphore(3)

# Function to display thread names with structured output
def display(name):
    # Acquire the semaphore before proceeding
    semaphore.acquire()
    try:
        for i in range(5):
            # Simulate work with a delay of 3 seconds
            time.sleep(3)
            # Print the thread name along with a timestamp and iteration count
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {name}: Iteration {i+1}")
    finally:
        # Release the semaphore to allow other threads to proceed
        semaphore.release()

# Create multiple threads with unique names
threads = [
    Thread(target=display, args=(f"Thread-{i+1}",)) for i in range(5)
]

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
