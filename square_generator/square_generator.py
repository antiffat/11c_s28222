import math
from abc import ABC, abstractmethod

# Task 6 (Modules):
# Task 10 (Abstract Elements):
class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass

    # Task 4 (Libraries):
    def calculate_square_roots(self, squares):
        if squares is None:
            raise ValueError("Input list cannot be None")
        return [math.sqrt(x) for x in squares]
