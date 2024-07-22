class shape:
    def calculate_area(self, num1, num2):
        self.num1 = num1
        self.num2 = num2        
        self.area = num1 * num2

class rectangle(shape):
    def calculate_area(self, num1, num2):
        return super().calculate_area(num1, num2)
        se
