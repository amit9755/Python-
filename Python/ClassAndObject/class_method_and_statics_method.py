#use of class method and statics method
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #using class method
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name,date.today().year-year)
    #statics method check adult or not
    @staticmethod
    def isadult(age):
        return age>18


Person1 = Person("Amit", 25)
Person2 = Person("Kushwah", 17)
print("I am {} and my age {}".format(Person1.name,Person1.age ))
print("I am {} and my age {}".format(Person2.name,Person2.age ))
Person1.fromBirthYear("Amit", 1997)
Person1.fromBirthYear("Kushwah", 2000)
print(Person1.age)
print(Person2.age)
print(Person1.isadult(34))
print(Person1.isadult(18))