# ticket booking
from random import randint

class train:
   
   def __init__(self, train_no):
      self.train_no = train_no
   def book(self,fro, to):
      print(f"your seat will be booked and your train no is {self.train_no} and your train departure from {fro} and destination is {to}")
   def getstatus(self):
      print(f"your train {self.train_no} is  running on time")
   def getfare(self,fro, to):
      print(f"your seat will be booked and your train no is {self.train_no} and your train departure from {fro} and destination is {to}\n you paid {randint(180,370)}")

t = train(20347)
t.book("delhi","bihar")
t.getstatus()
t.getfare("delhi","bihar")