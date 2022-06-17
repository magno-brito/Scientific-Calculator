from tarfile import PAX_FIELDS
from tkinter import ttk
from tkinter import*
window =  window = Tk()
window.title("Scientific Calculator")
window.geometry("700x500")
window.resizable(False, False)
window.rowconfigure(0, weight = 0)

scr = Label(window, relief = GROOVE, borderwidth = 4, text = "Ok", bg = '#B5E5E6', width=12, height=1)
scr.grid(column=0, row=0, padx= 5, pady=5)

scr1 = Label(window, relief = GROOVE, borderwidth = 4, text = "Not ok", bg = '#B5E5E6', width=12, height=1)
scr1.grid(column=2, row=2, padx= 5, pady=5)

window.mainloop()