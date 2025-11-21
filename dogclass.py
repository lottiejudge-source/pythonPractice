class Dog: 
    # this is initialising the name and age attributes - defining the data that all children of the dog parent class should have
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    # defining the behaviours (methods/functions) 
    def sit(self):
        print(f"{self.name} is now sitting. Good doggy!")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")

# creating an instance of the class 
my_dog = Dog('Watson', 9)
print(f"My dogs called {my_dog.name}. He's {my_dog.age} years old!")
# calling the methods within the class using dot notation
my_dog.sit()
my_dog.roll_over()