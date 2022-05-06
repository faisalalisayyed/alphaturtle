![Logo](https://raw.githubusercontent.com/C0DE-SLAYER/alphaturtle/master/img/logo.png)

    > To Draw Alphabet And Number Using Turtle Module

## About Turtle:
* This project is made using in-built python library called “Turtle”. 
* Turtle graphics is a popular way for introducing programming to kids. 
* It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966.

## Installation


#### Gui Installation [(How To Use)](#Usage):

```python
git clone https://github.com/C0DE-SLAYER/alphaturtle
cd alphaturtle
pip install -r requirement.txt
python alphaturtle_gui.py
```

#### To Use Function On Your Own / CLI [(How To Use)](#Usage) : 

```python
pip install alphaturtle
```
    
## Usage/Examples

#### Gui Usage :

1.Run using `python alphaturtle_gui.py` 

![App Screenshot](https://raw.githubusercontent.com/C0DE-SLAYER/alphaturtle/master/img/run_program.png)

2.Fill All The Requried Field

![App ScreenShot](https://raw.githubusercontent.com/C0DE-SLAYER/alphaturtle/master/img/fill_field.png)

3.Hit The Draw Button :

![App Screenshot](https://raw.githubusercontent.com/C0DE-SLAYER/alphaturtle/master/img/draw_button.png)

#### CLI Usage : 

If you have install alphaturtle using pip just run this in terminal/powershell/cmd :

    alphaturtle -i python

![App Screenshot](https://raw.githubusercontent.com/C0DE-SLAYER/alphaturtle/master/img/cli.png)

For help run `alphaturtle -h`

![App Screenshot](https://raw.githubusercontent.com/C0DE-SLAYER/alphaturtle/master/img/help.png)

#### Use Function Own :

Include alphaturtle in your project :

    from alphaturtle import * # import aplhaturtle 
    import turtle # importing turtle module
    SetVar(2, 5, 20, 'black', 'yellow', 0) # setting values

    drawLetterP() # calling function to draw P 
    whiteSpace()  # drawing whitespace
    drawLetterY() # calling function to draw Y 
    whiteSpace()  # drawing whitespace
    drawLetterT() # calling function to draw T 
    whiteSpace()  # drawing whitespace
    drawLetterH() # calling function to draw H 
    whiteSpace()  # drawing whitespace
    drawLetterO() # calling function to draw O 
    whiteSpace()  # drawing whitespace
    drawLetterN() # calling function to draw N 

    turtle.hideturtle() # turtle method to hide the cursor
    turtle.done() # To see the output

![App Screenshot](https://raw.githubusercontent.com/C0DE-SLAYER/alphaturtle/master/img/draw_button.png)

## Limitations

- The code works fine for all capatial alphabets and numericals ,but not for special characters except dot and hipan

## License

[MIT](https://github.com/C0DE-SLAYER/alphaturtle/blob/master/LICENSE.txt)

