import math

# Task 1:
squares = [x**2 for x in range(1, 11)]
print(squares)

# Task 2:
def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

squares = generate_squares(1, 10)
print("List of squares from 1 to 10: ", squares)

# Task 3:
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]

    # Task 4:
    def calculate_square_roots(self, squares):
        return [math.sqrt(x) for x in squares]

generator = SquareGenerator()
squares = generator.generate_squares(2, 8)
square_roots = generator.calculate_square_roots(squares)

print("List of squares from 2 to 8:", squares)
print("Square roots of the generated squares: ", square_roots)

