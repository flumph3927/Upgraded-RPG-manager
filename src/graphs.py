import matplotlib.pyplot as plt

#class DataVisualization
class DataVisualization:
    #initiate: character, optional second character
    def __init__(self, character, optional = None):
        #character is a dictionary of all the character's info
        self.char = character
        #optional is an optional second character for comparing
        self.char_two = optional
    #display
    def display(self):
        #set up the graph
        #set the catigories to the attributes
        categories = ['Strength', 'Speed', 'Magic']
        #get the info for the character and input it as the values for the catigories
        values = [self.char.str,self.char.spd,self.char.mag]
        #display the graph
        plt.bar(categories, values)
        plt.ylabel("Level")
        plt.title("Attribute Levels")
        plt.show(block=True)
    #compare
    def compare(self):
        #set up the graph
        #set the catigories to the attributes
        categories = ['Strength', 'Speed', 'Magic']
        #get the info for the character and input it as the values for the catigories
        values_one = [self.char.str,self.char.spd,self.char.mag]
        values_two = [self.char_two.str,self.char_two.spd,self.char_two.mag]
        #display the graph
        plt.subplot(1, 2, 1)
        plt.bar(categories, values_one)
        plt.title("Character 1 Attribute Levels")

        plt.subplot(1, 2, 2)
        plt.bar(categories, values_two)
        plt.title("Character 2 Attribute Levels")
        plt.tight_layout()
        plt.show(block=True)