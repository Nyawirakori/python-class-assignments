#Creating a class

class Animal:
    #constructor
    def __init__(self, name, habitat, legs):
        self.name = name
        self.habitat = habitat
        self.legs = legs
        self.food = self.type_of_food()
    #methods(should be verbs)
    def eating(self):
        self.type_of_food()

    def walking():
        pass
    def running():
        pass

    @classmethod
    def type_of_food(cls):
        return "I like food !"

#creating instances
dog = Animal("dog","domestic", 4)

print(dog.legs)