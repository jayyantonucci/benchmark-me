import msvcrt as m
import time, random

def wait():
    m.getch()

print('any key to start, press enter after random delay')
wait()

print('\n...get ready...\n')

time.sleep(random.randint(2,5))
print('PRESS ENTER')
time_start = time.time()
input()
time_end = time.time()
time_react = time_end - time_start
print('time ' + str(time_react) + ' seconds')


