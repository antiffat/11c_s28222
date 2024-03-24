from square_generator.square_generator import SquareGenerator

print("W")
# Task 1 (List Comprehensions):
squares = [x**2 for x in range(1, 11)]
print(squares)

# Task 2 (Functions):
def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

squares = generate_squares(1, 10)
print("List of squares from 1 to 10: ", squares)

# Task 8 (Inheritance):
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
    # Task 5 (Exceptions) is also inherited, so we need to handle if end < start
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [x**3 for x in range(start, end + 1)]

# usage of task 8:
generator = CubicGenerator()
cubes = generator.generate_squares(1, 5)
print(" Task 8: List of cubes from 1 to 5: ", cubes)

# Task 3 (Classes) (it is now moved to square_generator module):
generator = CubicGenerator() # I changed it from SquareGenerator to Cubic Generator because SquareGenerator is abstract after task 10.
try:
    squares = generator.generate_squares(1, 10)
    print("List of squares from 1 to 10:", squares)

    square_roots = generator.calculate_square_roots(squares)
    print("Square roots of the generated squares:", square_roots)

except ValueError as e:
    print(f"Error: {e}")
