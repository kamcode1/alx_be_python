# class Student:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(f"name of student is {self.name} and age is {self.age}")
# student1 = Student("kam", 35)
# student1.display()  

# class product:
#     def __init__(self, p_name, price, quantity):
#         self.name = p_name
#         self.price = price
#         self.quantity = quantity
    
#     def total_value(self):      
#         total_value_in_stock = self.price * self.quantity
#         return total_value_in_stock

### Encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        return f"I can walk"
    
    def __str__(self):
        return f"My name is {self.name} and i'm {self.age} years old"

# person1 = Person("kam", 35)
# person2 = Person("sam", 39)
# print(person1.walk())
# print(person1.age)
# print(person1.name)
# print(person1)
# print(person2)

### Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def enrol(self, course):
        self.course = course

student1 = Student("kam", 35, "WA1978")
print(student1.name, student1.age, student1. student_id)


### Polymorphisim
#class Undergraduate(Student)
