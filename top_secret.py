import time  # время
from tkinter import Tk, Label  # графика (*-all import from module)

root = Tk() 
root.title('Biba+Boba=Abobus')  # название окна
root.geometry('+10+10')   # позиция окна
g = Label(root, bg="red", fg="purple", text="alibabus", font="arial 90")
g.pack(ipadx=20, ipady=20)  # g.grid 


def gettime():
    p = ':' if int(time.strftime('%S')) % 2 == 0 else ' '
    g['text'] = time.strftime(f'%H{p}%M{p}%S')  # (f"%H{переменная}%M") f - функция
    g.after(1000,gettime)
 

gettime()


root.mainloop()

# import time as XZ
# XZ.strftime()