# EXERCISE 2: Create a Program with 2 child processes in Tree organization.

import time
from multiprocessing import Process


def pureCpuIntensive(x):
  sum=0
  for x in range(100000000):
    sum+=x

pidlist2 = []

def main():
    process = Process(target=pureCpuIntensive)
    process.start()
    pid = process.pid
    pidlist2.append(pid)
    process.join()

starttime2 = time.time()
if __name__ == '__main__':
    for i in range(2):
        main()
    print(pidlist2)
    endtime2 = time.time()
    print('Time elapsed: ' + str(endtime2 - starttime2))


    