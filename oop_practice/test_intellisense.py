class Example:
    def __init__(self):
        self.attribute = 42

    def method(self, value):
        self.attribute = value

example = Example()
example.attribute

example.method(10)
example.attribute