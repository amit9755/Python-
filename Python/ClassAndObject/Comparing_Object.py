class computer:
    def __init__(self):
        self.name = "Amit kushwah"
        self.age = 25
    def update(self):
        self.age = 30
    def compare(self,object):
        if self.age == object.age:
            return "Yes both are the equal!"
        else:
            return "Not equal !!"
c1 = computer()
c2 = computer()
print(c1.name)
print(c2.name)
c2.age = 35
print(c1.age)
print(c2.age)
c1.update()
print(c1.age)
print(c1.compare(c2))
