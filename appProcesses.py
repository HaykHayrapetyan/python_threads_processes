import timeit


codeChunk = """
import os
from multiprocessing import Process



def runShell(n):
    myCmd = ' dd if=/dev/zero of=/home/hayk/test/filename' + str(n) + '.txt count=102400 bs=1024'
    os.system(myCmd)
    

for i in range(0, 30):
    p = Process(target=runShell, args=(i,))
    p.start()

"""

elapsed_time = timeit.timeit(codeChunk, number=1) # 0.04405724297976121
print(elapsed_time)