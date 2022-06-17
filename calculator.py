from imp import get_suffixes
from tarfile import PAX_FIELDS
from tkinter import ttk
from tkinter import*
from math import*

from numpy import column_stack

class Calculator:
    def __init__(self):
       self.window=  Tk()
       self.window.title("Scientific Calculator")
       self.window.geometry("390x340")
       self.window.resizable(False, False)
       self.value = StringVar()
       self.expression = ""
       self.result = ""
       self.frame = Frame(self.window,  borderwidth = 4, bg = '#216158', width=350, height=340)
       self.frame.grid(padx = 7, pady = 5);
       self.frame1 = Frame(self.frame,  borderwidth = 4, bg = '#B5E5E6', width=70, height=20)
       self.frame1.grid(column = 0, row = 1, columnspan=10, padx = 2, pady = 5);
       self.scr = Entry(self.frame1,font="Helvetica 14", textvariable = self.value, bg = '#B5E5E6', insertwidth = 5, width=30 )
       self.scr.grid(column=6, row=1, padx= 2, pady=2, ipady=5, ipadx=10)
    

    def entry_values(self,value):
        new_value = self.value.get()
        self.value.set(new_value + value)
        self.expression = self.scr.get()

        
        

    def equal(self):
        π = pi
        self.value.set(round(eval(self.expression, {'π':pi}, globals()),4))
    def clear(self):
        self.value.set("")


    def numbers(self):
        color = '#9FBED6'
        one = Button(self.frame, text = '1',bg = color, command = lambda: self.entry_values('1'),font = ('Arial',14), width=3 )
        one.grid(column = 4 , row = 3, padx = 2, pady = 1.5)

        two = Button(self.frame, text = '2', bg = color, command = lambda: self.entry_values('2'), font = ('Arial',14), width=3 )
        two.grid(column = 5 , row = 3, padx = 2, pady = 1.5)

        three = Button(self.frame, text = '3', bg = color, command = lambda: self.entry_values('3'), font = ('Arial',14), width=3 )
        three.grid(column = 6 , row = 3, padx = 2, pady = 1.5)

        four = Button(self.frame, text = '4', bg = color, command = lambda: self.entry_values('4'), font = ('Arial',14), width=3 )
        four.grid(column = 4 , row = 4, padx = 2, pady = 1.5)

        five = Button(self.frame, text = '5', bg = color, command = lambda: self.entry_values('5'), font = ('Arial',14), width=3 )
        five.grid(column = 5 , row = 4, padx = 2, pady = 1.5)

        six = Button(self.frame, text = '6', bg = color, command = lambda: self.entry_values('6'), font = ('Arial',14), width=3 )
        six.grid(column = 6 , row = 4, padx = 2, pady = 1.5)

        seven = Button(self.frame, text = '7', bg = color, command = lambda: self.entry_values('7'), font = ('Arial',14), width=3 )
        seven.grid(column = 4 , row = 5, padx = 2, pady = 1.5)

        eight = Button(self.frame, text = '8', bg = color, command = lambda: self.entry_values('8'), font = ('Arial',14), width=3 )
        eight.grid(column = 5 , row = 5, padx = 2, pady = 1.5)

        nine = Button(self.frame, text = '9', bg = color, command = lambda: self.entry_values('9'), font = ('Arial',14), width=3 )
        nine.grid(column = 6 , row = 5, padx = 2, pady = 1.5)

        zero = Button(self.frame, text = '0', bg = color, command = lambda: self.entry_values('0'), font = ('Arial',14), width=3 )
        zero.grid(column = 4 , row = 6, padx = 2, pady = 1.5)

        dot = Button(self.frame, text = '.', bg = color, command = lambda: self.entry_values('.'), font = ('Arial',14), width=3 )
        dot.grid(column = 5 , row = 6, padx = 2, pady = 1.5)

        delete = Button(self.frame, text = 'CE', bg = '#0021E6', command = lambda: self.clear(),font = ('Arial',14), width=3 )
        delete.grid(column = 6, row = 6, padx = 2, pady = 1.5)

        ###########################################
        

    def basics_operation(self):
        color = '#A4CBED'
        symbol1 = Button(self.frame, text = '(', bg = color, command = lambda: self.entry_values('('),font = ('Arial',14), width=3 )
        symbol1.grid(column = 4 , row = 2, padx = 2, pady = 1.5)

        symbol2 = Button(self.frame, text = ')', bg = color, command = lambda: self.entry_values(')'),font = ('Arial',14), width=3 )
        symbol2.grid(column = 5 , row = 2, padx = 2, pady = 1.5)

        percent = Button(self.frame, text = '%', bg = color, command = lambda: self.entry_values('%'),font = ('Arial',14), width=3 )
        percent.grid(column = 6 , row = 2, padx = 2, pady = 1.5)

        division = Button(self.frame, text = '/', bg = color, command = lambda: self.entry_values('/'), font = ('Arial',14), width=3 )
        division.grid(column = 7 , row = 2, padx = 2, pady = 1.5)

        add = Button(self.frame, text = '+', bg = color, command = lambda: self.entry_values('+'),font = ('Arial',14), width=3 )
        add.grid(column = 7 , row = 3, padx = 2, pady = 1.5)

        sub = Button(self.frame, text = '-', bg = color, command = lambda: self.entry_values('-'),font = ('Arial',14), width=3 )
        sub.grid(column = 7 , row = 4 ,padx = 2, pady = 1.5)

        mul = Button(self.frame, text = "x", bg = color, command = lambda: self.entry_values('*'),font = ('Arial',14), width=3)
        mul.grid(column = 7 , row = 5 , padx = 2, pady = 1.5)

        div = Button(self.frame, text = '÷', bg = color, command = lambda: self.entry_values('/'), font = ('Arial',14), width=3)
        div.grid(column = 7, row = 6 , padx = 2, pady = 1.5 )

    def trigonometry_functions(self):
        super_s = "⁻¹"
        color = '#008EE6'
        sin = Button(self.frame, text = 'sin', bg = color, command = lambda: self.entry_values('sin'), font = ('Arial',14), width=4)
        sin.grid(column = 0 , row =2 , padx =  2, pady = 1.5 , sticky=W)

        cos = Button(self.frame, text = 'cos', bg = color, command = lambda: self.entry_values('cos'), font = ('Arial',14), width=4)
        cos.grid(column = 0 , row =3 , padx =  1, pady = 1.5 , sticky=W)

        tan = Button(self.frame, text = 'tan', bg = color, command = lambda: self.entry_values('tan'), font = ('Arial',14), width=4)
        tan.grid(column = 0 , row =4 , padx =  1, pady = 1.5 , sticky=W)

        arcsin = Button(self.frame, text = 'sin' + super_s, bg = color, command = lambda: self.entry_values('arcsin'), font = ('Arial',14), width=4)
        arcsin.grid(column = 1 , row =2 , padx =  1, pady = 1.5 , sticky=W)

        arccos = Button(self.frame, text = 'cos' + super_s, bg = color, command = lambda: self.entry_values('arccos'), font = ('Arial',14), width=4)
        arccos.grid(column = 1 , row =3 , padx =  1, pady = 1.5 , sticky=W)

        arctan = Button(self.frame, text = 'tan' + super_s, bg = color, command = lambda: self.entry_values('arctan'), font = ('Arial',14), width=4)
        arctan.grid(column = 1 , row =4 , padx =  1, pady = 1.5 , sticky=W)

        rad = Button(self.frame, text = 'RAD', bg = color, command = lambda: self.entry_values('rad'),font = ("Arial",14), width=4)
        rad.grid(column = 2, row = 2, padx = 2, pady = 1.5)

        degree = Button(self.frame, text = 'DEG', bg = color, command = lambda: self.entry_values('deg'),font = ("Arial",14), width=4)
        degree.grid(column = 2, row = 3, padx = 2, pady = 1.5)

        pi = Button(self.frame, text = 'π', bg = color, command = lambda: self.entry_values('π'), font = ("Arial",14), width=4)
        pi.grid(column = 2, row = 4, padx = 2, pady = 1.5)
    
    def expo_functions(self):
        color3 = '#69B9F0'
        super_s = "ⁿ"
        square = Button(self.frame,text = '√', bg = color3, command = lambda: self.entry_values('√'), font = ("Arial",14), width=4)
        square.grid(column = 0, row = 5, padx = 2, pady = 1.5)

        power2 = Button(self.frame, text = 'x²', bg = color3, command = lambda: self.entry_values('²'), font = ("Arial",14), width=4)
        power2.grid(column = 1, row = 5, padx = 2, pady = 1.5)

        power = Button(self.frame, text = 'x'+ super_s,  command = lambda: self.entry_values('^'), bg = color3, font = ("Arial",14), width=4)
        power.grid(column = 2, row = 5, padx = 2, pady = 1.5)

        exp = Button(self.frame,text = 'ENG', bg = color3, command = lambda: self.entry_values('eng'),font = ("Arial",14), width=4)
        exp.grid(column = 0, row = 6, padx = 2, pady = 1.5)

        log = Button(self.frame,text = 'log', bg = color3, command = lambda: self.entry_values('log'), font = ("Arial",14), width=4)
        log.grid(column = 1, row = 6, padx = 2, pady = 1.5)

        ln = Button(self.frame,text = 'ln', bg = color3, command = lambda: self.entry_values('ln'), font = ("Arial",14), width=4)
        ln.grid(column = 2, row = 6, padx = 2, pady = 1.5)


        euler = Button(self.frame, text = 'e', bg = color3, command = lambda: self.entry_values('e'), font = ("Arial",14), width=4)
        euler.grid(column = 2, row = 7, padx = 2, pady = 1.5)

        abs = Button(self.frame, text = 'abs', bg = color3, command = lambda: self.entry_values('abs'),font = ("Arial",14), width=4)
        abs.grid(column = 0, row = 7, padx = 2, pady = 1.5)

        log2 = Button(self.frame, text = 'log2', bg = color3,  command = lambda: self.entry_values('log2'),font = ("Arial",14), width=4)
        log2.grid(column = 1, row = 7, padx = 2, pady = 1.5)
    
    def fat(self):
        color = '#69B9F0'
        fat = Button(self.frame, text = 'n!', bg = color,  command = lambda: self.entry_values('!'), font = ("Arial",14), width=3)
        fat.grid(column = 4, row = 7, padx = 2, pady = 1.5)

        combinacao = Button(self.frame, text = 'nCr', bg = color, command = lambda: self.entry_values('C'),font = ("Arial",14), width=3)
        combinacao.grid(column = 5, row = 7, padx = 2, pady = 1.5)

        ans = Button(self.frame, text = 'ANS', bg = color, command = lambda: self.entry_values('ans'), font = ("Arial",14), width=3)
        ans.grid(column = 6, row = 7, padx = 2, pady = 1.5)

        final = Button(self.frame, text = '=', bg = "#0021E6", command = lambda: self.equal(), font = ("Arial",14), width=3)
        final.grid(column = 7, row = 7, padx = 2, pady = 1.5)
    



    def gerar(self):
        self.trigonometry_functions()
        self.basics_operation()
        self.expo_functions()
        self.numbers()
        self.fat()
        self.window.mainloop()
        

janela = Calculator()
janela.gerar()