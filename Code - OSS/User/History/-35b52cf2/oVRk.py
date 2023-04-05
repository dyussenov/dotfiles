from tkinter import *  

#----------------------------------
  
def clicked():  
    res = "Привет {}".format(txt.get())  
    lbl.configure(text=res)  

#----------------------------------  
window = Tk()
window.title("my first app")
window.geometry('400x250')
#----------------------------------

#Label - вывести текст на экран
lbl = Label(window, text="Привет")
lbl.grid(column=0, row=0) #задать месторасположение элемента

#Entry - окошко для ввода данных
txt = Entry(window,width=10)
txt.grid(column=1, row=0)


btn = Button(window, text="Клик!", command=clicked)
btn.grid(column=2, row=0)

#----------------------------------
window.mainloop()