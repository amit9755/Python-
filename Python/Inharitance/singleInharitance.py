import os
import time
import logging

class Person(object):
    #instance attribute
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    #class method
    def detail(self):
        print("----------Person class details function-------------")
        print("my name is  {}".format(self.name))
        print("my Idnumber is {}".format(self.idnumber))

    def show(self):
        print("----------Person class show function -------------")
        print(self.name)
        print(self.idnumber)

class Employee(Person):
    def __init__(self,name, idnumber , salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,idnumber)

    def detail(self):
        print("----------Employee class details function-------------")
        print("my name is  {}".format(self.name))
        print("my idnumber is {}".format(self.idnumber))
        print("my salary is  {}".format(self.salary))
        print("my Post is {}".format(self.post))


obj_Employee = Employee("Amit kushwah", 1400, 800000, "Software Engineer")
obj_Employee.detail()
obj_Employee.show()

