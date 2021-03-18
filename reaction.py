import os
import msvcrt as m
import time, random
from datetime import datetime

f = open('reaction_times.txt', 'a+')
os.system('cls')
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime('%d-%b-%Y (%H:%M:%S)')

def reaction():
    print('Reaction test\n')
    react_times = []
    print('Set test count to at least 5 to save average.')
    test_count = int(input('set test count: '))
    print('press any key to start\n\n')
    m.getch()

    for i in range(test_count):
        print(f'...get ready... {i+1} of {test_count}')
        time.sleep(random.randint(2,5))
        time_start = time.time()
        input('PRESS ENTER')
        time_end = time.time()
        time_react = time_end - time_start
        if time_react < 0.01:
            print('too soon junior...') 
            quit()
        print(f'time: {time_react:.3f} seconds\n\n')
        react_times.append(time_react)

    react_avg = sum(react_times)/len(react_times)
    print(f'Average time: {react_avg:.3f} seconds')
    if test_count >= 5:
        f = open('reaction_times.txt', 'a+')
        f.write(f'{timestampStr}: Average time: {react_avg:.3f} seconds ({test_count} tests.) \r')
        f.close()
    
    while True:
        Prompt = input("run it back? answer y or n\n")
        if Prompt in ['y', 'yes']:
            reaction()
        elif Prompt in ['n', 'no']:
            quit()
        

reaction()
