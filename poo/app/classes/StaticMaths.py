class StaticMath:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
    def __new__(cls, *args, **kwargs):
        # Prevent instantiation
        raise TypeError("StaticMath class cannot be instantiated." )
# Example usage:
# result = StaticMath.add(5, 3)

class StaticMathDAughter(StaticMath):
    def example_method(self):
        return "This is a method in the daughter class."
    def suoper_method(self):
        return super().add(2,3)