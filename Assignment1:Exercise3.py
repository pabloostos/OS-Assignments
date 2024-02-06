# EXERCISE3: Create a Program with 5 child Threads.
import time
import os
import threading

def pureCpuIntensive():
  sum=0
  for x in range(100000000):
    sum+=x

threads = []
def main():
    thread = threading.Thread(target=pureCpuIntensive)
    threads.append(thread)
    thread.start()

starttime3 = time.time()
if __name__ == "__main__":
    for i in range(5):
        print('Thread ' + str(i))
        main()
    
    for thread in threads:
        thread.join()

    endtime3 = time.time()
    print('Time elapsed: ' + str(endtime3 - starttime3))


    