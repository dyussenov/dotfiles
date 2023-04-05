from tkinter import *
import random

# ----------------------------------
Game_status = "start"

def clicked():
    shoot = random.randint(1,6)
    if shoot == 1:
        res = "СМЭРТЬ"
    else:
        res = "Хорошая работа Олег"
    lbl.configure(text=res)
def was_ded_become_dead(widgets_to_forget, widgets_to_show):
    for w in widgets_to_forget:
        w.pack_forget()
    for w in widgets_to_show:
        w.pack

# ----------------------------------
window = Tk()
window.title("БАН ГАН")
window.geometry('1360x680')
# ----------------------------------
lbl1 = Label(window, text="Суета рулет")
lbl1.grid(column=0, row=1)  # задать месторасположение элемента

btn1 = Button(window, text="Нажми на кнопку получишь результат!", command=clicked)
btn1.grid(column=2, row=1)

lbl = Label(window, text="сколько вас бедолаг?")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

btn = Button(window, text="Ехала", command=was_ded_become_dead)
btn.grid(column=2, row=0)


# Label - вывести текст на экран


# ----------------------------------
window.mainloop()