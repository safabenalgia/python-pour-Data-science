def somme (x,y):
    return x+y
#print("hello")
from math import sqrt
class Point:
 def __init__(self,x,y) :
        self.x=x
        self.y=y
 def afficher(self):
    print("Point ",self.x,",",self.y) 
 def __str__(self):
    return "Point"+str(self.x)+","+str(self.y)
 def decaler(self ,t1,t2):
    self.x+=t1
    self.y+=t2
 def distance (self,p):
    d=sqrt((self.x-p.x)**2+(self.y-p.y)**2)
    return d