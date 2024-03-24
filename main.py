from square_generator.square_generator import SquareGenerator

# Task 1 (List Comprehensions):
squares = [x**2 for x in range(1, 11)]
print(squares)

# Task 2 (Functions):
def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

squares = generate_squares(1, 10)
print("List of squares from 1 to 10: ", squares)

# Task 3 (Classes) (it is now moved to square_generator module):

generator = SquareGenerator()
try:
    squares = generator.generate_squares(1, 10)
    print("List of squares from 1 to 10:", squares)

    square_roots = generator.calculate_square_roots(squares)
    print("Square roots of the generated squares:", square_roots)

except ValueError as e:
    print(f"Error: {e}")


