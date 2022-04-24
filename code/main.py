from tkinter import *

LogText = ''
def gui():
    root = Tk()
    root.title("hello world")
    root.geometry('300x300')
    root.configure(background='white')
    Label(root, text='222', font=('Arial', 20)).pack()

    frm = Frame(root)
    # left
    frm_L = Frame(frm)
    Label(frm_L, text='222', font=('Arial', 15)).pack(side=TOP)
    Label(frm_L, text='333', font=('Arial', 15)).pack(side=TOP)
    frm_L.pack(side=LEFT)

    # right
    frm_R = Frame(frm)
    Label(frm_R, text='444', font=('Arial', 15)).pack(side=TOP)
    Label(frm_R, text='555', font=('Arial', 15)).pack(side=TOP)
    frm_R.pack(side=RIGHT)

    frm.pack()
    root['bg']='#FFFFFF'

    root.mainloop()
if __name__ == '__main__':
    gui()

