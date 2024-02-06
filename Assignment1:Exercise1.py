# EXERCISE 1: Create a Program with 5 child processes in parallel.
import time
import os
from multiprocessing import Process

def pureCpuIntensive(x):
  sum=0
  for x in range(100000000):
    sum+=x

processes = []
pidlist1 = []

def main():
    process = Process(target=pureCpuIntensive, args=('ChildProcess',))
    processes.append(process)
    process.start()
    pid = process.pid
    pidlist1.append(pid)

if __name__ == '__main__':
    starttime1 = time.time()
    for i in range(5):
        main()

    for process in processes:
        process.join()
    
    endtime1 = time.time()
    print(pidlist1)
    print('Time elapsed: ' + str(endtime1 - starttime1))
    

    