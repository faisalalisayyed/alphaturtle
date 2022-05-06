import argparse
import alphaturtle as cli
import turtle

def main():
    parser = argparse.ArgumentParser(description='alphaturtle - To Draw Alphabet And Number Using Turtle Module')

    parser.add_argument("-i", "--input", type = str, nargs = 1, default = None, help = "Enter the string to draw", required=True)

    parser.add_argument("-t", "--thickness", type = int, nargs = 1, default = 2, help = "Define the thickness of letter") 

    parser.add_argument("-sp", "--spacing", type = int, nargs = 1, default = 5, help = "Define spacing between the letter") 

    parser.add_argument("-s", "--size", type = int, nargs = 1, default = 20, help = "Define size of the letter",action='store') 

    parser.add_argument("-c", "--color", type = str, nargs = 1, default = 'black', help = "Define colour of the letter") 

    parser.add_argument("-bg", "--bgcolor", type = str, nargs = 1, default = 'white', help = "Define background colour of the window") 

    parser.add_argument("-sd", "--speed", type = int, nargs = 1, default = 1, help = "Define the speed of drawing a letter") 

    args = parser.parse_args()

    if args.thickness == 2:
        thickness = 2
    else:
        thickness = args.thickness[0]
    
    if args.spacing == 5:
        spacing = 5
    else:
        spacing = args.spacing[0]

    if args.size == 20:
        size = 20
    else:
        size = args.size[0]

    if args.speed == 1:
        speed = 1
    else:
        speed = args.speed[0]

    Input = ''.join(args.input)
    color = ''.join(args.color)
    bgcolor = ''.join(args.bgcolor)
    
    cli.SetVar(thickness,spacing,size,color,bgcolor,speed)
    userInput(Input)

def userInput(userInput):

    userInput = str(userInput)
    userInput = userInput.lower()

    for c in userInput:
        if c == 'a':
            cli.drawLetterA()
            cli.whiteSpace()
        elif c == 'b':
            cli.drawLetterB()
            cli.whiteSpace()
        elif c == 'c':
            cli.drawLetterC()
            cli.whiteSpace()
        elif c == 'd':
            cli.drawLetterD()
            cli.whiteSpace()
        elif c == 'e':
            cli.drawLetterE()
            cli.whiteSpace()
        elif c == 'f':
            cli.drawLetterF()
            cli.whiteSpace()
        elif c == 'g':
            cli.drawLetterG()
            cli.whiteSpace()
        elif c == 'h':
            cli.drawLetterH()
            cli.whiteSpace()
        elif c == 'i':
            cli.drawLetterI()
            cli.whiteSpace()
        elif c == 'j':
            cli.drawLetterJ()
            cli.whiteSpace()
        elif c == 'k':
            cli.drawLetterK()
            cli.whiteSpace()
        elif c == 'l':
            cli.drawLetterL()
            cli.whiteSpace()
        elif c == 'm':
            cli.drawLetterM()
            cli.whiteSpace()
        elif c == 'n':
            cli.drawLetterN()
            cli.whiteSpace()
        elif c == 'o':
            cli.drawLetterO()
            cli.whiteSpace()
        elif c == 'p':
            cli.drawLetterP()
            cli.whiteSpace()
        elif c == 'q':
            cli.drawLetterQ()
            cli.whiteSpace()
        elif c == 'r':
            cli.drawLetterR()
            cli.whiteSpace()
        elif c == 's':
            cli.drawLetterS()
            cli.whiteSpace()
        elif c == 't':
            cli.drawLetterT()
            cli.whiteSpace()
        elif c == 'u':
            cli.drawLetterU()
            cli.whiteSpace()
        elif c == 'v':
            cli.drawLetterV()
            cli.whiteSpace()
        elif c == 'w':
            cli.drawLetterW()
            cli.whiteSpace()
        elif c == 'x':
            cli.drawLetterX()
            cli.whiteSpace()
        elif c == 'y':
            cli.drawLetterY()
            cli.whiteSpace()
        elif c == 'z':
            cli.drawLetterZ()
            cli.whiteSpace()
        elif c == '0':
            cli.drawNumber0()
            cli.whiteSpace()
        elif c == '1':
            cli.drawNumber1()
            cli.whiteSpace()
        elif c == '2':
            cli.drawNumber2()
            cli.whiteSpace()
        elif c == '3':
            cli.drawNumber3()
            cli.whiteSpace()
        elif c == '4':
            cli.drawNumber4()
            cli.whiteSpace()
        elif c == '5':
            cli.drawNumber5()
            cli.whiteSpace()
        elif c == '6':
            cli.drawNumber6()
            cli.whiteSpace()
        elif c == '7':
            cli.drawNumber7()
            cli.whiteSpace()
        elif c == '8':
            cli.drawNumber8()
            cli.whiteSpace()
        elif c == '9':
            cli.drawNumber9()
            cli.whiteSpace()
        elif c == '-':
            cli.drawdash()
            cli.whiteSpace()
        elif c == '.':
            cli.drawdot()
            cli.whiteSpace()
        elif c == ' ':
            cli.whiteSpace()
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()