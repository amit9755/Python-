import logging
import os
import time

logging.basicConfig(filename="Accessing_class_member.log", format='%(asctime)s, %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
class Dog:
    #class attributes
    attri = "mammel"
    #instance attributes
    def __init__(self, name):
        self.name = name
    #class method
    def speak(self):
        print("I am a {}".format(self.name))

#Driver code
#object initilize
Roadger = Dog("Roadger")
Tommy = Dog("Tommy")
#Accessing class attributes
print("I am a {}".format(Roadger.__class__.attri))
print("I am a {}".format(Tommy.__class__.attri))
logger.debug(Roadger.__class__.attri)
logger.debug(Tommy.__class__.attri)
#Accessing instance attribute
print("I am a {}".format(Roadger.name))
print("I am a {}".format(Tommy.name))
logger.debug(Roadger.name)
logger.debug(Tommy.name)
#Accessing class method
Roadger.speak()
Tommy.speak()
logger.debug(Roadger.speak())
logger.debug(Tommy.speak())
