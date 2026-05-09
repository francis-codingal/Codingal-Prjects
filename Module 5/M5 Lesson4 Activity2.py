class Computer:

    def __init__(self):
        self.__maxprice = 1200

    def sell(self):
        print("Current Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

laptop = Computer()
laptop.sell()
laptop.__maxprice = 1500
laptop.sell()

laptop.setMaxPrice(1500)
laptop.sell()