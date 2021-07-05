from super_thread import SuperThread
import time

# Function
def greet(name):
    while(True):
        print(name)

# Start a Thread
my_thread = SuperThread('Test', lambda: greet('John'))
my_thread.start()

# Terminate a Thread
my_thread.terminate() # 1
SuperThread.terminate_by_name('Test') # 2
SuperThread.terminate_all() # 3

# Get Active Threads
print(SuperThread.active_threads)
