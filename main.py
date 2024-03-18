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
        # Task 5
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [x ** 2 for x in range(start, end + 1)]

    # Task 4:
    def calculate_square_roots(self, squares):
        return [math.sqrt(x) for x in squares]

generator = SquareGenerator()
try:
    squares = generator.generate_squares(1, 10)
    print("List of squares from 1 to 10:", squares)

    square_roots = generator.calculate_square_roots(squares)
    print("Square roots of the generated squares:", square_roots)

except ValueError as e:
    print(f"Error: {e}")

