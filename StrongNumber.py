import math
def is_strong_number(num: int) -> bool:
    """Check if a number is a Strong Number."""
    total = 0
    for digit in str(num):
        total += math.factorial(int(digit))
    return total == num
# Example usage
number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a Strong Number!")
else:
    print(f"{number} is NOT a Strong Number.")