# parent class
class Person(object):	

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)

# child class
class Employee(Person):		
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def display_employee(self):
        # Calling the parent display method
        self.display() 
        print("Salary:", self.salary)
        print("Post:", self.post)

# creation of an object instance
a = Employee('Rahul', 886012, 200000, "Intern")	

# Displaying all information
a.display_employee()