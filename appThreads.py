import timeit


codeChunk = """
import os
import threading



def runShell(n):
    myCmd = ' dd if=/dev/zero of=/home/hayk/test/filename' + str(n) + '.txt count=102400 bs=1024'
    os.system(myCmd)
    
threads = list()
for i in range(0, 30):
    x = threading.Thread(target=runShell, args=(i,))
    print(threading.activeCount())
    threads.append(x)
    x.start()

# uncomment this if you won't main thread to become idle until other threads end
# for thread in threads:  
    # thread.join()
"""

elapsed_time = timeit.timeit(codeChunk, number=1) # 0.41187096398789436
print(elapsed_time)