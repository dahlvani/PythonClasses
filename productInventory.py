class Product:

    #Initialises attributes
    def __init__(self,productId,name,price,quantity):

        self.id = productId
        self.name = name
        self.price = price
        self.quantity = quantity

    #Updates the product's price
    def updatePrice(self,new_price):

        if new_price > 0:
            self.price = new_price
        else:
            print "Sorry! The price of a product must be greater than 0"


#Update the quantity of the product by incrementing or decrementing
    def updateQuantity(self,new_quantity,isIncrement):

        if isIncrement is True:
            self.quantity += new_quantity
        elif (self.quantity - new_quantity) >= 0:
            self.quantity -= new_quantity
        else:
            print "Error, cannot reduce further!"

    #Returns the current quantity of the product.
    def getQuantity(self):

        return self.quantity

    #Displays product info
    def viewProduct(self):

        print "Product ID: " + str(self.id) + ", Name: " + self.name + ", Price: " + \
        str(self.price) + ", Quantity: " + str(self.quantity)

#Initialize attribute
class Inventory:
    def __init__(self):

        self.listProd = []

    #Add new product to list
    def addProduct(self,productID):

        self.listProd.append(productID)

    #removes roduct from the list
    def removeProduct(self,productID):
        if productID in self.listProd:
            self.listProd.remove(productID)
        else:
            print "Error. Product is not in the inventory."

    #Display inventory
    def viewInventory(self):
        print self.listProd

if __name__ == '__main__':
    prod1 = Product(1,"shampoo",2.20,5)
    print prod1.getQuantity()
    prod1.updateQuantity(2,True)
    prod1.viewProduct()

    invent1 = Inventory()
    invent1.addProduct(1)
    invent1.removeProduct(2)
    invent1.viewInventory()
