import os
import msvcrt as m
import time, random

os.system("cls")


def reaction():
    print('Reaction test\n')
    react_times = []
    print('any key to start, PRESS ENTER after random delay\n')
    m.getch()
    
    for i in range(3):
        print('...get ready...')
        time.sleep(random.randint(2,5))
        print('PRESS ENTER')
        time_start = time.time()
        input()
        time_end = time.time()
        time_react = time_end - time_start
        if time_react < 0.01:
            print('too soon junior...')
            quit()
        print(f'time: {time_react:.3f} seconds\n\n')
        react_times.append(time_react)

    print(react_times)
    react_avg = sum(react_times)/len(react_times)
    print(f'Average time: {react_avg:.3f} seconds')

reaction()
