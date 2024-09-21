# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None
    __inventory: Inventory = None

    # Constructor
    def __init__(self, sale: Sale = None, inventory: Inventory = None):
        self.__lastSale = sale
        self.__inventory = inventory

    # Setter method for LastSale
    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    # Getter method for LastSale
    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale
    
    # Getter method for item 
    def __getitem__(self, item):
        return self

    # Getter method for Inventory
    @property
    def getInventory(self) -> Inventory:
        return self.__inventory

class Inventory:
    def __init__(self, quantity: int):
        self.quantity = quantity


# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    # Constructor 
    def __init__(self, products: List[Product]): #, saleNumber: int = 1):
        Sale.__saleTimes += 1
        self.__products = products
        self.__saleNumber = Sale.__saleTimes
        
        for product in products:
            product.setLastSale(self)
            product.getInventory.quantity -= 1 

    # Setter method for ProductsSold
    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    # Returns the last sale the item was sold
    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber

# Test
productOne = Product(inventory=Inventory(quantity=7))
productTwo = Product(inventory=Inventory(quantity=5))

saleOne = Sale([productOne, productTwo])
saleTwo = Sale([productOne])
saleThree = Sale([productTwo])

print(f"{productOne.getLastSale.getSaleNumber}, {productTwo.getLastSale.getSaleNumber}")

print(f"productOne Inventory After Sales: {productOne.getInventory.quantity}")
print(f"productTwo Inventory After Sales: {productTwo.getInventory.quantity}")
