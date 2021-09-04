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
#Accessing instance attribute
print("I am a {}".format(Roadger.name))
print("I am a {}".format(Tommy.name))
#Accessing class method
Roadger.speak()
Tommy.speak()
