import datetime
#URBAN PLANNER

#In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city. Create a class named Building in the building.py file and define the following fields, properties, and methods.
class Building:

    def __init__(self, address, stories):
        self.designer = "Dustin Hobson"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

#Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

    def construct(self):
        self.date_constructed = datetime.datetime.now()

#Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.

    def purchase(self, name):
        self.owner = name
#Create 5 building instances
#Have each one get purchased by a real estate magnate
#After purchased, construct each one
#Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.



