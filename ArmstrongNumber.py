# Function to check Armstrong number
def is_armstrong(number):
    # Convert number to string to iterate over digits
    digits = str(number)
    n = len(digits)  # number of digits
    sum_of_powers = 0
    for digit in digits:
        # Raise digit to the power n and add to sum_of_powers
        sum_of_powers += int(digit) ** n
    # Check if sum_of_powers equals the original number
    if sum_of_powers == number:
        return True
    else:
        return False
# Example usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")