from cira.ciragame import *

class MyGame(CiraGame):

    # declare variables here
    fruits = 'apple', '' # add your own fruit here
    veggies = 'spinach', '' # add your own vegetable here
    fruitsAndVeggies = fruits + veggies
    # this is where we will print our variables to see their contents
    print fruits
    print veggies
    print fruitsAndVeggies
