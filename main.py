# Task 1:
squares = [x**2 for x in range(1, 11)]
print(squares)

# Task 2:
def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

squares = generate_squares(1, 10)
print("List of squares from 1 to 10: ", squares)

