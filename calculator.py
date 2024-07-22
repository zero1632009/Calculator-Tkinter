from tkinter import *

root = Tk()
root.title("Calculator")
root.minsize(height=500, width=400)

screen = StringVar()

entry = Entry(root, textvariable=screen, font=("JetBrains Mono", "30"))
entry.place(x=0, y=0, width=400, height=100)

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "AC":
        screen.set("")
    else:
        current_text = screen.get()
        new_text = current_text + text
        screen.set(new_text)

def btn(txt, ht, wth, tx, ty):
    button = Button(root, text=txt, height=ht, width=wth)
    button.place(x=tx, y=ty)
    button.bind("<Button-1>", button_click)
    return button

btn1 = btn("0", 2, 6, 10, 450)
btn2 = btn(".", 2, 6, 120, 450)
btn3 = btn("=", 2, 6, 225, 450)
btn4 = btn("/", 2, 6, 325, 450)

btn5 = btn("7", 2, 6, 10, 380)
btn6 = btn("8", 2, 6, 120, 380)
btn7 = btn("9", 2, 6, 225, 380)
btn8 = btn("*", 2, 6, 325, 380)

btn9 = btn("4", 2, 6, 10, 310)
btn10 = btn("5", 2, 6, 120, 310)
btn11 = btn("6", 2, 6, 225, 310)
btn12 = btn("-", 2, 6, 325, 310)

btn13 = btn("1", 2, 6, 10, 240)
btn14 = btn("2", 2, 6, 120, 240)
btn15 = btn("3", 2, 6, 225, 240)
btn16 = btn("+", 2, 6, 325, 240)

btn17 = btn("AC", 2, 6, 325, 170)

root.mainloop()
