
class Animal(object):
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Hi! My name is {self.name}, I am an animal.")

class Whale(Animal):
    def __init__(self, name, species):
        super(Whale, self).__init__(name)
        self.species = species

    def say_hi(self):
        super(Whale, self).say_hi()
        print(f"To be more specific, I am a whale from the {self.species} species.")


pepe = Animal('Pepe')
pepe.say_hi()

juan = Whale('Juan', 'orca')
juan.say_hi()