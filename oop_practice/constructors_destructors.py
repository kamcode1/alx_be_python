# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __del__(self):
#         print("object being deleted goodbye")

# obj = Person("bag", 4)
# del obj

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"'{self.title}'by {self.author} and number of pages:{self.pages}"
    
#     def __repr__(self):
#         return f"Book(title = '{self.title}', author = '{self.author}', pages = {self.pages})"
    
# book1 = Book("Lord of the Ring", "Kam Noah", 250)

# print(str(book1))
# print(repr(book1))

class Animal:


    def eat(self):
        print(f"This animal is eating.")
    
    def sleep(self):
        print(f"This animal is sleeping.")

class Dog(Animal):

    def bark(self):
        print(f"This Dog is Barking out of his lung!")
    
animal = Animal()
dog = Dog()

animal.eat()
animal.sleep()

dog.eat()
dog.sleep()
dog.bark()