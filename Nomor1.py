import json


class Color:
    def __init__(self, color, size):
        self.color = color
        self.size = self.__setSize(size)

    def __setSize(self, size):
        if isinstance(size, list):
            return size
        else:
            return None

    def getJSON(self):
        return {'color' : self.color,
                'size' : self.size}


class Product:
    def __init__(self, itemID, itemName, price, color, freeShipping):
        self.itemID = self.__setItemID(itemID)
        self.itemName = self.__setItemName(itemName)
        self.price = self.__setPrice(price)
        self.freeShipping = self.__setFreeShipping(freeShipping)
        self.availableSizeAndColor = self.__setAvailableColorAndSize(color)

    def __setItemID(self, itemID):
        if isinstance(itemID, str):
            return itemID
        else:
            return None

    def __setItemName(self, itemName):
        if isinstance(itemName, str):
            return itemName
        else:
            return None

    def __setPrice(self, price):
        if isinstance(price, int):
            return price
        else:
            return None

    def __setAvailableColorAndSize(self, color):
        data = {}
        data['availableColorAndSize'] = []
        if isinstance(color, list):
            for c in color:
                data['availableColorAndSize'].append(c.getJSON())
            return data
        else:
            return None

    def __setFreeShipping(self, freeShipping):
        if isinstance(freeShipping, bool):
            return freeShipping
        else:
            return None

    def getJSON(self):
        return {'itemID' : self.itemID,
                'itemName' : self.itemName,
                'price' : self.price,
                'availableColorAndSize' : self.availableSizeAndColor,
                'freeShipping' : self.freeShipping}


if __name__ == '__main__':
    data = {}

    data['product'] = []
    color = Color("blue-black", ["M", "L"])
    color2 = Color("black", ["M"])

    colorList = [color, color2]

    product = Product("12341822", "FGX Flannel Shirt", 195000, colorList, False)
    product2 = Product("111111", "Casual Shirt", 79000, colorList, True)
    products = [product, product2]

    for p in products:
        data['product'].append(p.getJSON())

    print json.dumps(data, indent=4)
