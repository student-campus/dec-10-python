class Math:
    a = 10
    b = 11


obj = Math()
obj1 = Math()
obj1.c = 1100
print(obj1.c)
obj2 = Math()
print(obj2.a)
print("..." * 6)


class Science:
    s = 10
    y = 11

    def add(self):
        return self.s + self.y


obj = Science()
print(obj.add())


class Math:
    a = 100
    b = 345

    def __init__(self):
        print("hello i. am here")  # Not return

    def add(self):
        self.c = 10
        print(self.c)
        return self.a + self.b

    def sub(self):
        self.add()
        return self.add() - self.b


obj = Math()


class Balance:
    def __init__(self, accouht_number, holder_name, account_type, initial_bal, status):
        self.account_number = accouht_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.initial_bal = initial_bal
        self.status = status

    def minbal(self):
        if self.initial_bal == 0:
            return "account has zero "
        return f"{self.initial_bal}"

    def requirement(self):
        self.saving = 1000
        if self.initial_bal >= self.saving:
            self.status = "active"
            return f"{self.status}"
        else:
            self.status = "inactive"
            return f"{self.status}"


c1 = Balance(4567, "Saru", "Individual", 15000, Balance.requirement)
print(c1.minbal())
print(c1.requirement())
print("Account status", c1.status)


# increasing code reusability
class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary


harry = Employee("harry", "jackson", 44000)
rohan = Employee("rohan", "Das", 12000)


print(rohan.lname, harry.lname)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


ram = Student("ram", 20)
print(ram.name)
print(ram.age)


# it doesnot use return
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


rect = Rectangle(4, 5)
print(rect.area())


# class and instance variable
class Employe:
    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = Employe.increment * self.salary


hari = Employe("hari ", "prasad", 23000)
sita = Employe("sita", "shergil", 3400)
print(hari.salary)
hari.increase()
print(hari.salary)


# Inheritance
# Single INheritance
class Parent:

    a = 10
    b = 20

    def __init__(self, a):
        print("iam cons from parent class", a)


class Child(Parent):
    a = 1111
    d = 1

    def __init__(self, c):
        print("iam cons from child")
        super().__init__(2333)
        # object is present at child class


obj = Child(23)

print(f"..." * 5)


class Person:
    def __init__(self, name):
        self.name = name

    def func(self):
        return f"The person name is {self.name}"


class Child(Person):
    def __init__(self, name, student_id):
        self.student_id = student_id
        super().__init__(name)

    def func2(self):
        return f" The child details is name as {self.name} and ID as {self.student_id}"


obj = Child("Rita", 345)
print(obj.func())
print(obj.func2())


# Multilevel inheritance
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_people(self):
        return f"The name is {self.name} and age is {self.age}"


class Patient(People):
    def __init__(self, name, age, patient_id):
        self.patient_id = patient_id
        super().__init__(name, age)

    def display_patient(self):
        return f" The patient ID {self.patient_id} of a person is {self.name} and age is {self.age}"


class InPatient(Patient):
    def __init__(self, name, age, patient_id, room_number):
        self.room_number = room_number
        super().__init__(name, age, patient_id)

    def display_inpatient(self):
        return f"The {self.name} and age is {self.age} and room_number is {self.room_number}"


obj = InPatient("ram", 23, 345, 200)
print(obj.display_patient())
print(obj.display_people())
print(obj.display_inpatient())
