from dataclasses import dataclass
import random


@dataclass
class Member:
    name :str
    height:float
    weight:float

    @property
    def name(self)-> str:return self._name

    @name.setter
    def name(self,name): self._name = name

    @property
    def weight(self)-> float:return self._weight
    
    @weight.setter
    def weight(self,weight): self._weight = weight

    @property
    def height(self)->float:return self._height

    @height.setter
    def height(self,height):self._height = height

def myRandom(start, end): return random.randint(start, end)
def my100(): return myRandom(1, 100)



