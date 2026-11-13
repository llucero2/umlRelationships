class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, title, employees):
        self.title = title
        self.employees = employees  

    def show_team(self):
        names = [emp.name for emp in self.employees]
        print(f"{self.title} team: {', '.join(names)}")


alice = Employee("Alice")
bob = Employee("Bob")

it_dept = Department("IT", [alice, bob])
it_dept.show_team()  

del it_dept
print(alice.name)    # Output: Alice