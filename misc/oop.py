import numpy as np

class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")

# Inheritence
class Student(People):

    # This is an attribute of the class, which is for all of the objects
    n_instances = 0

    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa
        Student.n_instances += 1

    # Overrides the People's greet()
    def greet(self):
        print(f"Hello {self.name}, you are a student")

    def state_gpa(self):
        print(f'You have a {self.gpa}')

# Encapsulation
class Private_Person(People):
    def __init__(self, name, age, pin):
        super().__init__(name, age)
        self.__pin = pin

    def get_pin(self):
        return self.__pin

me = People("Om", 15)
me.greet()
# me.set_name("Bob")
# me.greet()

another = Student("Bob", 18, 4.0)
another.greet()
another.state_gpa()

pp = Private_Person("Unknown", 50, 3221)
# print(pp.__pin) # Python will not let you do this, so it is private
print(pp.get_pin()) # This is the only way to access them

# print(np.random.randint(-10, 10, (3, 2)))