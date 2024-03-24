import math

# Task 6 (Modules):
class SquareGenerator:
    def generate_squares(self, start, end):
        # Task 5 (Exceptions):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [x ** 2 for x in range(start, end + 1)]

    # Task 4 (Libraries):
    def calculate_square_roots(self, squares):
        return [math.sqrt(x) for x in squares]
