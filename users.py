class Users:
    def __init__(self, first_name, surname):
        self.first_name = first_name 
        self.surname = surname 
    
    def describe_user(self):
        print(f"{self.first_name}{self.surname}")
    
    def greeting(self):
        print(f"stay breezy {self.first_name}")

john_constantine = Users("John", "Constantine")
john_constantine.greeting()

lily_allen = Users("Lily", "Allen")
lily_allen.greeting()

idris_elba = Users("Idris", "Elba")
idris_elba.greeting()
