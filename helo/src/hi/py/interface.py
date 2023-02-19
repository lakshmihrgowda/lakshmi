import abc
class Food (abc.ABC):
    @abc.abstractmethod
    def taste( self ):
        pass
class north_indian(Food) :
    def taste(self):
        print(" Cooking! ")
s = north_indian ()
print( isinstance(s, Food))
