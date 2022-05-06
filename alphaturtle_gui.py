import tkinter as tk
from tkinter.messagebox import showwarning
from alphaturtle_cli import userInput
from colour import Color
import re
from alphaturtle import SetVar

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('580x350')
        self.resizable(False,False)
        self.title('AlphaTurtle')
        self.fs = 'HelvLight 11'

    def FrameTop(self):
        f1 = tk.Frame(self)
        f1.pack(side=tk.TOP, fill=tk.BOTH)

        # label
        tk.Label(f1,text='Welcome to AlphaTurtle...',font='Magneto 18 bold').pack()
        tk.Label(f1).pack()
        tk.Label(f1,text='Enter The Sentence To Draw:',font=self.fs).pack(anchor=tk.W, padx=5)

        # entry here
        self.Einputtext = tk.Entry(f1, relief=tk.RIDGE,border=2,font=50)
        self.Einputtext.pack(padx=5, pady=5, fill=tk.X,ipady=2,ipadx=2)

    def FrameLeft(self):
        f2 = tk.Frame(self)
        f2.pack(side=tk.LEFT, fill=tk.BOTH)

        # label
        tk.Label(f2,).grid(row=1)
        tk.Label(f2,text='Size :',font=self.fs).grid(row=2, column=0, padx=5,sticky=tk.W)
        tk.Label(f2).grid(row=3)
        tk.Label(f2 ,text='Color :',font=self.fs).grid(row=4, column=0, padx=5,sticky=tk.W)
        tk.Label(f2).grid(row=5)
        tk.Label(f2,text='BG Color :',font=self.fs).grid(row=6,column=0,padx=5,sticky=tk.W)
        tk.Label(f2).grid(row=7)
        tk.Button(f2,text='Help Me!',font=self.fs).grid(row=8,column=1)

        # entry here
        self.Esize = tk.Entry(f2,relief=tk.RIDGE,border=2)
        self.Esize.grid(row=2, column=1, padx=5, pady=5)
        self.Ecolor = tk.Entry(f2,relief=tk.RIDGE,border=2)
        self.Ecolor.grid(row=4, column=1, padx=5, pady=5)
        self.Ebgcolor = tk.Entry(f2,relief=tk.RIDGE,border=2)
        self.Ebgcolor.grid(row=6, column=1, padx=5, pady=5)

    def FrameRight(self):
        f3 = tk.Frame(self)
        f3.pack(side=tk.RIGHT, fill=tk.BOTH)

        # label
        tk.Label(f3).grid(row=1)
        tk.Label(f3, text='Thickness :',font=self.fs).grid(row=2,sticky=tk.W)
        tk.Label(f3).grid(row=3)
        tk.Label(f3, text='Spacing :',font=self.fs).grid(row=4,sticky=tk.W)
        tk.Label(f3).grid(row=5)
        tk.Label(f3,text='Drawing Speed :',font=self.fs).grid(row=6,sticky=tk.W)
        tk.Label(f3).grid(row=7)

        # entry here
        self.Ethickness = tk.Entry(f3,relief=tk.RIDGE,border=2)
        self.Ethickness.grid(row=2, column=1, padx=5, pady=5)
        self.Espacing = tk.Entry(f3,relief=tk.RIDGE,border=2)
        self.Espacing.grid(row=4, column=1, padx=5, pady=5)
        self.Espeed = tk.Entry(f3,relief=tk.RIDGE,border=2)
        self.Espeed.grid(row=6, column=1, padx=5, pady=5)

        # button here
        tk.Button(f3,text='Draw It!', command=self.CallingFun).grid(row=8, column=0)
        tk.Button(f3,text='Reset!', command=self.Reset).grid(row=8, column=1)

    def Reset(self):
        self.Einputtext.delete(0,'end')
        self.Esize.delete(0,'end')
        self.Ecolor.delete(0,'end')
        self.Ebgcolor.delete(0,'end')
        self.Ethickness.delete(0,'end')
        self.Espacing.delete(0,'end')
        self.Espeed.delete(0,'end')

    def CallingFun(self):
        # getter the value and storing it
        Gthickness = self.Ethickness.get()
        Gspacing = self.Espacing.get()
        Ginputtext = self.Einputtext.get()
        Gsize = self.Esize.get()
        Gcolor = self.Ecolor.get()
        Gbgcolor = self.Ebgcolor.get()
        Gspeed = self.Espeed.get()
        
        # check for empty value and not runing the turtle
        flag = True

        # check for input and pass it to main function
        if Gthickness.isdigit():
            Gthickness = int(Gthickness)
        elif Gthickness == '':
            showwarning('warning','Thickness Should Not Be Empty.')
            flag = False
        else:
            showwarning('warning','Thickness Should Be In Number.')
            flag = False

        if Gspacing.isdigit():
            Gspacing = int(Gspacing)
        elif Gspacing == '':
            showwarning('warning','Spacing Should Not Be Empty.')
            flag = False
        else:
            showwarning('warning','Spacing Should Be In Number.')
            flag = False

        if Gsize.isdigit():
            Gsize = int(Gsize)
        elif Gsize == '':
            showwarning('warning','Size Should Not Be Empty.')
            flag = False
        else:
            showwarning('warning','Size Should Be In Number.')
            flag = False

        if Gspeed == '0' or Gspeed == '1':
            Gspeed = int(Gspeed)
        elif Gspeed == '':
            showwarning('warning','Speed Should Not Be Empty.')
            flag = False
        else:
            showwarning('warning','Speed Should Be 0 For fast or 1 For Slow')
            flag = False

        try:
            if Gthickness == '':
                showwarning('warning','Colour Should Not Be Empty.')
                flag = False
            else:
                print(Color(Gcolor.replace(' ','')))
        except:
            showwarning('warning','The Colour You Enter Is Not A Valid Colour')
            flag = False

        try:
            if Gthickness == '':
                showwarning('warning','Bg Colour Should Not Be Empty.')
                flag = False
            else:
                print(Color(Gbgcolor.replace(' ','')))
        except:
            showwarning('warning','The BgColour You Enter Is Not A Valid Colour')
            flag = False

        if Ginputtext == ' ' or Ginputtext == '':
            showwarning('Warning','The Input is Empty')
            flag = False

        # checking for the symbol in input
        symbol = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
        if flag == True:
            if symbol.search(Ginputtext) == None:
                SetVar(Gthickness,Gspacing,Gsize,Gcolor,Gbgcolor,Gspeed)
                userInput(Ginputtext)
            else:
                showwarning('warning','we cannot draw it check the string')


if __name__ == '__main__':
    gui = GUI()
    gui.FrameTop()
    gui.FrameLeft()
    gui.FrameRight()
    gui.mainloop()
