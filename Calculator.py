from tkinter import *


def click(event):
    global sc_value
    text = event.widget.cget('text')

    if text == '=':
        if sc_value.get().isdigit():
            value = int(sc_value.get())
        else:
            try:
                value = eval(e.get())
            except Exception:
                print('Wrong use of operator')
                value = 'ERROR'

        sc_value.set(value)
        e.update()

    elif text == 'C':
        sc_value.set('')
        e.update()
    else:
        sc_value.set(sc_value.get() + text)
        e.update()


root = Tk()

# Main window
root.geometry('370x450')
root.configure(bg='yellow')
p1 = PhotoImage(file='calculator.ico')
root.iconphoto(False, p1)
root.title('CALCULATOR')

# Input area
sc_value = StringVar()
sc_value.set('')
e = Entry(root, textvar=sc_value, font='Times 45 bold')
e.pack(fill=X, pady=10, padx=10)

# frame and buttons
f = Frame(root, bg='blue')
lists = [1, 2, 3, '+', 4, 5, 6, '-', 7, 8, 9, '*', 'C', 0, '=', '/']
count = 0
for r in range(4):
    for c in range(4):
        b = Button(f, width=3, height=1, text=str(lists[count]), font="Times 30 bold")
        b.grid(row=r, column=c, padx=2, pady=2)
        b.bind("<Button-1>", click)
        count += 1
f.pack()

root.mainloop()
