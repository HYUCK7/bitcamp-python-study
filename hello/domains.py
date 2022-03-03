from dataclasses import dataclass


@dataclass
class Member:
    name :str
    height:float
    weight:float
    kor : int
    eng : int
    math : int

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

    @property
    def kor(self)-> int: return self._kor

    @kor.setter
    def kor(self,kor):self._kor = kor


