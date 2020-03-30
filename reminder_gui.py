from tkinter import *
window = Tk()
window.title("Reminder GUI App")
window.geometry('600x600')
lbl = Label(window, text="ReminderApp", font=("Arial Bold", 25))
lbl.pack()
Label(window, text='Remind you about?')
e1 = Entry(window)
window.mainloop()