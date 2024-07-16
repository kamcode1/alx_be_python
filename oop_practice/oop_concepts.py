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
        self.course = []

    def enrol(self, course):
        self.course.append(course)
        return f"{self.name} enrolled in {self.course}"

    def __str__(self):
        return f"{self.name}{self.age}{self.walk()}"

# student1 = Student("kam", 35, "WA1978")
# print(student1.enrol("Maths"))
# print(student1.enrol("English"))
#print(student1.name, student1.age, student1. student_id)

### Polymorphisim
class Undergraduate(Student):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age, student_id)
        self.major = major
    def enrol(self, course):
        if len(self.course) < 2:
            return super().enrol(course)
        else:
            return f"cannot enrol{self.name} in the {self.course}"
    def __str__(self):
        return f"{self.name} {self.age} {self.student_id} {self.major}"

ungrad = Undergraduate("kam", 35, "WA1978", "Tech")    
# print(ungrad)
# print(ungrad.enrol("SE"))
# print(ungrad.enrol("Economics"))
# print(ungrad.enrol("IT"))
# print(ungrad.enrol("Art"))

### Abstraction

def new_enrolment(student, course):
    return student.enrol(course)

enroll = new_enrolment(ungrad, "Spanish")
print(enroll)