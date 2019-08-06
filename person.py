import re


class Person:

    __id = 0

    def __init__(self, fName, lName, email, phones, address, YoB):
        self.validate(fName, lName, email, phones, address, YoB)
        self.__FirstName = fName
        self.__email = email
        self.LastName = lName
        self.phones = phones
        self.address = address
        self.__birthyear = YoB
        self.ID = self.generatID()



    @classmethod
    def generatID(cls):
        cls.__id += 1
        return cls.__id

    @staticmethod
    def checkEmail(email):
        return re.search("^[\w]*@.*hwltd\.com$",email)

    def validate(self, fName, lName, email, phones, address, YoB):
        if fName == "" or lName == "":
            raise ValueError("person's name is not valid")
        if not self.checkEmail(email):
            raise ValueError("person's email is not valid "+str(email))

    def add_phone(self,pNum):
        self.phones.append(pNum)

    def delete_phone(self,pNum):
        self.phones.remove(pNum)

    def changead(self,ad):
        self.address=ad

    def getEmail(self):
        return self.__email

    def getFirstName(self):
        return self.__FirstName



class Phone:
    def __init__(self, number):
        self.checkPhone(number)
        self.Number=number

    @staticmethod
    def checkPhone(number):
        if not re.search("^[\+\d][\d\-]+$", number):
            raise ValueError("phone number is nut valid "+number)
        return


class Address:
    def __init__(self, country, city):
        self.city = city
        self.country = country

    def tostring(self):
        return "{}, {}".format(self.city, self.country)


class StreetAddress(Address):
    def __init__(self, country, city, st, housenum):
        super().__init__(country, city)
        self.street = st
        self.houseNumber = housenum

    def tostring(self):
        return super().toStrng()+" {}, {}".format(self.street, self.houseNumber)


class PobAddress(Address):
    def __init__(self, country, city, POB):
        super().__init__(country, city)
        self.POB=POB

        def tostring(self):
            return super.toStrng() + " {}".format(self.POB)
