
class Product_info:
    def __init__(self,pid=None, name=None, price=None, qnt=None, manufact=None, contact=None):
        self.__productid = pid
        self.__name = name
        self.__price = price
        self.__quantity = qnt
        self.__manufacturer = manufact
        self.__contact = contact

    def set_productid(self,pid):
        self.__productid = pid

    def get_productid(self):
        return self.__productid

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_quantity(self, qnt):
        self.__quantity = qnt

    def get_quantity(self):
        return self.__quantity

    def set_manufacturer(self, manufact):
        self.__manufacturer = manufact

    def get_manufacturer(self):
        return self.__manufacturer

    def set_contact(self, contact):
        self.__contact= contact

    def get_contact(self):
        return self.__contact






