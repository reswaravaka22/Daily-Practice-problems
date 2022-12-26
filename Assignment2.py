"""
2.Write a class called Item that represents an item for sale. It should have the following:
      • Fields representing the name and price of the item
      • A constructor that sets those fields,
      • A __str__() method that returns a string containing the item name and price, with the price
      formatted to exactly 2 decimal places
      Test the class by creating a new item object and printing it out
"""

class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        print("ITEM FOR SALE...!")
        print("Item Name:{}  Price:{}".format(self.name,self.price))
p1=Item("Pen",10)
p1.__str__()