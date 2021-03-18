from tkinter import *

#init window
app = Tk()

part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0)

app.title('part manager')
app.geometry('500x500')

app.mainloop()