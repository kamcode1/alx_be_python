# class Book:
#     total_books = 0
    
#     def __init__(self, name):
#         self.name = name
#         Book.total_books += 1
        

#     @classmethod
#     def display_total_books(cls):
#         print(f"{cls.total_books}")


# book1 = Book("money")
# book2 = Book("karate kid")
# Book.display_total_books()

# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return a + b
    
#     @staticmethod
#     def multiply(a, b):
#         return a * b
    

# calculator1 = Calculator()
# print(calculator1.add(3, 6))
# print(calculator1.multiply(3, 6))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def create_child(cls, name):

       return cls(name, 0)

person1 = Person.create_child("kam")
print(person1.name)
print(person1.age)

    