from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

    def get_age(self):
        return f"{self.__age} (note this age is privately accessed)"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age()}")

    @abstractmethod
    def role(self):
        pass



class Student(Person):
    def study(self):
        print(f"{self.name} is studying!")

    def role(self):
        print(f"{self.name} is a student!")


class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching!")

    def role(self):
        print(f"{self.name} is a teacher!")


student1 = Student("Halin", 2)
student1.display_info()
student1.study()
student1.role()

print()

teacher1 = Teacher("Gralin", 30)
teacher1.display_info()
teacher1.teach()
teacher1.role()
