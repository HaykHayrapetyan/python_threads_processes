import timeit

codeChunk = """
import os

for i in range(0, 30):
    myCmd = ' dd if=/dev/zero of=/home/hayk/test/filename' + str(i+1) + '.txt count=102400 bs=1024'
    os.system(myCmd)
"""

elapsed_time = timeit.timeit(codeChunk, number=1)
print(elapsed_time) # 6.217759819002822 seconds
