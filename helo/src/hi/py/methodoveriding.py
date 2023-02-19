class Vehicle:        # define parent class
   def run(self):
       print ('Vehicle is running')

class Bike (Vehicle): # define child class
   def run(self):
      print ('Bike is running')

c = Bike()          # instance of child
c.run()         # child calls overridden method

