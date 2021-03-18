from tkinter import *

app = Tk()
app.title('reaction test TK')
app.geometry('500x500')

#functions
def start_test():
    pass


#buttons
start_btn = Button(app, text='start test', width=12, command=start_test)
start_btn.place(relx=0.5, rely=0.1, anchor=CENTER)


app.mainloop()