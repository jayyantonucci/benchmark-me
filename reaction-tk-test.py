import os
import msvcrt as m
import time, random
from datetime import datetime
from tkinter import *

os.system('cls')
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime('%d-%b-%Y (%H:%M:%S)')
app = Tk()
app.title('reaction test TK')
app.geometry('500x500')



#functions
def start_test():
    test_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
    #time.sleep(random.randint(2,5))
    #test_btn = Button(app, text='click!', width=24, height=12, bg='green')
    #test_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

#buttons
start_btn = Button(app, text='start test', width=24, height=2, command=start_test)
test_btn = Button(app, text='...wait...', width=24, height=12, bg='yellow')
start_btn.place(relx=0.5, rely=0.1, anchor=CENTER)




app.mainloop()