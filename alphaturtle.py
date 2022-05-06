import turtle


def SetVar(Lthickness,Lspacing,Lsize,Lcolor,Lbgcolor,Lspeed):
    turtle.pensize(Lthickness)
    turtle.color(Lcolor)
    turtle.bgcolor(Lbgcolor)
    turtle.speed(Lspeed)
    SetVar.letterspacing = Lspacing
    SetVar.letterSize = Lsize

def drawLetterA():
    turtle.seth(70)
    turtle.fd(SetVar.letterSize)
    turtle.seth(-70)
    turtle.fd(SetVar.letterSize)
    turtle.bk(SetVar.letterSize/2)
    turtle.seth(180)
    turtle.fd(SetVar.letterSize/3)
    turtle.bk(SetVar.letterSize/3)
    turtle.seth(-70)
    turtle.fd(SetVar.letterSize/2)


def drawLetterB():
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    for i in range(2):
        turtle.seth(0)
        turtle.fd(SetVar.letterSize/4)
        turtle.circle(-SetVar.letterSize/4, 180)
        turtle.fd(SetVar.letterSize/4)
    turtle.pu()
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.pd()


def drawLetterC():
    turtle.pu()
    turtle.fd(SetVar.letterSize/2+SetVar.letterSize/4)
    turtle.pd()
    turtle.bk(SetVar.letterSize/4)
    turtle.circle(SetVar.letterSize/2, -180)
    turtle.bk(SetVar.letterSize/4)
    turtle.pu()
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)
    turtle.pd()


def drawLetterD():
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/5)
    turtle.circle(-SetVar.letterSize/2, 180)
    turtle.fd(SetVar.letterSize/5)
    turtle.pu()
    turtle.bk(SetVar.letterSize/2+SetVar.letterSize/4)
    turtle.pd()


def drawLetterE():
    turtle.seth(0)
    for i in range(2):
        turtle.fd(SetVar.letterSize/2)
        turtle.bk(SetVar.letterSize/2)
        turtle.seth(90)
        turtle.fd(SetVar.letterSize/2)
        turtle.seth(0)
        if i == 1:
            turtle.fd(SetVar.letterSize/2)
    turtle.pu()
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)
    turtle.pd()


def drawLetterF():
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.bk(SetVar.letterSize/2)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize/2)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.pu()
    turtle.seth(270)
    turtle.fd(SetVar.letterSize/2)
    turtle.pd()


def drawLetterG():
    turtle.seth(0)
    turtle.pu()
    turtle.fd(SetVar.letterSize/2+SetVar.letterSize/4)
    turtle.pd()
    turtle.bk(SetVar.letterSize/4)
    turtle.circle(SetVar.letterSize/2, -180)
    turtle.bk(SetVar.letterSize/4)
    turtle.seth(270)
    turtle.pu()
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize/2)
    turtle.seth(180)
    turtle.fd(SetVar.letterSize/5)
    turtle.bk(SetVar.letterSize/5)
    turtle.seth(90)
    turtle.bk(SetVar.letterSize/2)


def drawLetterH():
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.bk(SetVar.letterSize/2)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize/2)
    turtle.bk(SetVar.letterSize)
    turtle.fd(SetVar.letterSize)


def drawLetterI():
    turtle.seth(0)
    turtle.fd(SetVar.letterSize)
    turtle.bk(SetVar.letterSize/2)
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.bk(SetVar.letterSize)
    turtle.pu()
    turtle.fd(SetVar.letterSize)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)
    turtle.pd()


def drawLetterJ():
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.circle(SetVar.letterSize/4, 90)
    turtle.fd(SetVar.letterSize/2+SetVar.letterSize/4)
    turtle.seth(180)
    turtle.fd(SetVar.letterSize/2)
    turtle.pu()
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)
    turtle.pd()


def drawLetterK():
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.bk(SetVar.letterSize/2)
    turtle.seth(0)
    turtle.fd(3)
    turtle.seth(45)
    turtle.fd(SetVar.letterSize-SetVar.letterSize/3)
    turtle.bk(SetVar.letterSize-SetVar.letterSize/3)
    turtle.seth(-45)
    turtle.fd(SetVar.letterSize-SetVar.letterSize/3)


def drawLetterL():
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.bk(SetVar.letterSize)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)


def drawLetterM():
    for i in range(2):
        turtle.seth(-285)
        turtle.fd(SetVar.letterSize)
        turtle.seth(-75)
        turtle.fd(SetVar.letterSize)


def drawLetterN():
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.seth(310)
    turtle.fd(SetVar.letterSize+SetVar.letterSize/3)
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.bk(SetVar.letterSize)


def drawLetterO():
    turtle.seth(0)
    turtle.pu()
    turtle.fd(SetVar.letterSize/2)
    turtle.pd()
    turtle.circle(SetVar.letterSize/2)
    turtle.pu()
    turtle.fd(SetVar.letterSize/2)
    turtle.pd()


def drawLetterP():
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/5)
    turtle.circle(-SetVar.letterSize/4, 180)
    turtle.fd(SetVar.letterSize/5)
    turtle.pu()
    turtle.seth(270)
    turtle.fd(SetVar.letterSize-SetVar.letterSize/4)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.pd()


def drawLetterQ():
    turtle.pu()
    turtle.fd(SetVar.letterSize/2)
    turtle.pd()
    turtle.circle(SetVar.letterSize/2)
    turtle.circle(SetVar.letterSize/2, 45)
    turtle.seth(-45)
    turtle.bk(SetVar.letterSize//3)
    turtle.fd((SetVar.letterSize//3)*2)


def drawLetterR():
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.circle(-SetVar.letterSize/4, 180)
    turtle.seth(300)
    turtle.fd(SetVar.letterSize/2)
    turtle.bk(SetVar.letterSize/2)
    turtle.seth(180)
    turtle.fd(SetVar.letterSize/2)
    turtle.pu()
    turtle.seth(270)
    turtle.fd(SetVar.letterSize-SetVar.letterSize/4)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2+SetVar.letterSize/4)
    turtle.pd()


def drawLetterS():
    turtle.seth(0)
    turtle.pu()
    turtle.fd(SetVar.letterSize/2)
    turtle.seth(90)
    turtle.fd(SetVar.letterSize/2+SetVar.letterSize/4)
    turtle.pd()
    turtle.seth(90)
    turtle.circle(SetVar.letterSize/4, 270)
    turtle.circle(-SetVar.letterSize/4, 270)
    turtle.pu()
    turtle.bk(SetVar.letterSize/4)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.pd()


def drawLetterT():
    turtle.seth(0)
    turtle.pu()
    turtle.fd(SetVar.letterSize/2)
    turtle.pd()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.bk(SetVar.letterSize)
    turtle.pu()
    turtle.fd(SetVar.letterSize)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)
    turtle.pd()


def drawLetterU():
    turtle.seth(90)
    turtle.pu()
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.bk(SetVar.letterSize/3+SetVar.letterSize/3)
    turtle.circle(-SetVar.letterSize/3, -180)
    turtle.bk(SetVar.letterSize/3+SetVar.letterSize/3)
    turtle.pu()
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)
    turtle.pd()


def drawLetterV():
    turtle.seth(90)
    turtle.pu()
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(285)
    turtle.fd(SetVar.letterSize)
    turtle.seth(75)
    turtle.fd(SetVar.letterSize)
    turtle.pu()
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)
    turtle.pd()


def drawLetterW():
    turtle.seth(90)
    turtle.pu()
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    for i in range(2):
        turtle.seth(285)
        turtle.fd(SetVar.letterSize)
        turtle.seth(75)
        turtle.fd(SetVar.letterSize)
    turtle.pu()
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)
    turtle.pd()


def drawLetterX():
    turtle.seth(90)
    turtle.pu()
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(315)
    turtle.fd(SetVar.letterSize+SetVar.letterSize/4)
    turtle.bk((SetVar.letterSize+SetVar.letterSize/4)/2)
    turtle.seth(225)
    turtle.fd((SetVar.letterSize+SetVar.letterSize/4)/2)
    turtle.bk(SetVar.letterSize+SetVar.letterSize/4)
    turtle.pu()
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)
    turtle.pd()


def drawLetterY():
    turtle.seth(90)
    turtle.pu()
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(315)
    turtle.fd(SetVar.letterSize/2+SetVar.letterSize/4)
    turtle.seth(45)
    turtle.fd(SetVar.letterSize/2+SetVar.letterSize/4)
    turtle.back(SetVar.letterSize/2+SetVar.letterSize/4)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize/2)
    turtle.pu()
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.pd()


def drawLetterZ():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(0)
    turtle.fd(SetVar.letterSize)
    turtle.seth(225)
    turtle.fd(SetVar.letterSize+SetVar.letterSize/3)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize)


def drawNumber1():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize/2)
    turtle.pd()
    turtle.seth(240)
    turtle.bk(SetVar.letterSize/2)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)


def drawNumber2():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(0)
    for i in range(5):
        turtle.fd(SetVar.letterSize/2)
        turtle.right(90)
        if i == 2 or i == 3:
            turtle.left(180)


def drawNumber3():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(0)

    @staticmethod
    def for3():
        turtle.fd(SetVar.letterSize/2)
        turtle.right(90)
    for i in range(6):
        for3()
        if i == 2:
            turtle.seth(0)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)


def drawNumber4():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(270)
    for i in range(3):
        turtle.fd(SetVar.letterSize/2)
        turtle.left(90)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)


def drawNumber5():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.bk(SetVar.letterSize/2)
    for i in range(4):
        turtle.right(90)
        turtle.fd(SetVar.letterSize/2)
        if i == 0:
            turtle.left(180)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)


def drawNumber6():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.bk(SetVar.letterSize/2)
    for i in range(5):
        turtle.right(90)
        turtle.fd(SetVar.letterSize/2)
        if i == 0:
            turtle.left(180)
    turtle.bk(SetVar.letterSize/2)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)


def drawNumber7():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)


def drawNumber8():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(0)

    @staticmethod
    def forUp():
        turtle.fd(SetVar.letterSize/2)
        turtle.right(90)
    for i in range(8):
        forUp()
        if i == 3:
            turtle.seth(270)
            turtle.fd(SetVar.letterSize/2)
            turtle.left(90)
    turtle.fd(SetVar.letterSize/2)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize/2)


def drawNumber9():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(0)

    @staticmethod
    def forUp():
        turtle.fd(SetVar.letterSize/2)
        turtle.right(90)
    for i in range(7):
        forUp()
        if i == 3:
            turtle.seth(270)
            turtle.fd(SetVar.letterSize/2)
            turtle.left(90)
    turtle.seth(0)
    turtle.fd(SetVar.letterSize/2)


def drawNumber0():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(SetVar.letterSize)
    turtle.pd()
    turtle.seth(0)
    for i in range(2):
        turtle.fd(SetVar.letterSize/2)
        turtle.right(90)
        turtle.fd(SetVar.letterSize)
        turtle.right(90)
    turtle.fd(SetVar.letterSize/2)
    turtle.seth(270)
    turtle.fd(SetVar.letterSize)


def drawdot():
    turtle.pu()
    turtle.seth(0)
    turtle.fd(3)
    turtle.seth(90)
    turtle.fd(2)
    turtle.pd()
    turtle.dot()
    turtle.pu()
    turtle.seth(270)
    turtle.fd(2)
    turtle.pd()


def drawdash():
    turtle.pu()
    turtle.seth(90)
    turtle.fd(10)
    turtle.pd()
    turtle.seth(0)
    turtle.fd(10)
    turtle.pu()
    turtle.seth(270)
    turtle.fd(10)
    turtle.pd()


def whiteSpace():
    xvalue = turtle.xcor()
    turtle.pu()
    turtle.goto(xvalue + SetVar.letterspacing, 0)
    turtle.pd()
