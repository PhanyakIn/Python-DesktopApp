import tkinter as tk

window = tk.Tk()
window.title('AppTest')
window.minsize(width=500, height=500)

a = 0

def addNumbers():
    global a
    global amountClick

    a += 1

    amountClick.pack_forget()

    amountClick = tk.Label(master=window, text=a)
    amountClick.pack(pady=20)

button = tk.Button(master=window,text="Click Me",command=addNumbers)
button.pack()

amountClick = tk.Label(master=window, text=a)
amountClick.pack()

window.mainloop()
