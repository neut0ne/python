# These are templates for manufacturing British coins. 
# Running the program will present a list of all coins and their properties.
# There are some default properties that all coins will inherit, and then
# there are unique properties for each child class of coins.

import random # Needed for the ability to Flip and land on Heads or Tails randomly!

class Coin(object):
    def __init__(self, rare = False, clean = True, heads = True, **kwargs): # **kwargs packs down all the Coin parent data into a dictionary called kwargs, making Coin able to accept keyword args from child classes.

        for key, value in kwargs.items(): # loops through all items in the child class dictionary and appends the keyword args to all other items in the parent class. Should generally work for any dictionary in parent/child class relationships.
            setattr(self, key, value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin spent!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self): # cleans up output of final, complete string. Defines what comes out when you print that object.
        if self.original_value >= 1.00:
            return "£{} coin".format(int(self.original_value))
        else:
            return "{}p coin".format(int(self.original_value * 100))

class One_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
            }
        super(One_Pence, self).__init__(**data)    

class Two_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
            }
        super().__init__(**data)

class Five_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None, # Polymorfism: overriding standard behaviour from parent class, because silver coins don't rust! 
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour # this is _polymorphism_, multiple definitions of functions. Overrides parent function.

        def clean(self):
            self.colour = self.clean_colour

class Ten_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.50
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

class Twenty_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5.00
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour
    
        def clean(self):
            self.colour = self.clean_colour

class Fifty_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.70,
            "mass": 8.00
            }
        super().__init__(**data)
    
        def rust(self):
            self.colour = self.clean_colour
    
        def clean(self):
            self.colour = self.clean_colour

class Pound(Coin): # class child_of(parent)
    def __init__(self):
        data = { # this is a dictionary with unique data pairs for this child class
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
            }
        super().__init__(**data) # unpacks the data from the dictionary, making the data keyword args.

class Two_Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 2.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 28.4,
            "thickness": 2.50,
            "mass": 12.00
            }
        super().__init__(**data)
    
# A list of our coin types (all coin child classes):
Coins = [One_Pence(), Two_Pence(), Five_Pence(), Ten_Pence(), Twenty_Pence(), Fifty_Pence(), Pound(), Two_Pound()]

for Coin in Coins:
    arguments = [Coin, Coin.colour, Coin.value, Coin.diameter, Coin.thickness, Coin.num_edges, Coin.mass]
    # Unpack above arguments to this string:
    string = "{}, colour:{}, value{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
    print(string)



