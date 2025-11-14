# ADDREV – Adding Reversed Numbers

def reverse_number(num_str):
    return int(num_str[::-1])  # reverse string and remove leading zeros

def main():
    N = int(input())
    for _ in range(N):
        A, B = input().split()
        # Reverse both numbers
        revA = reverse_number(A)
        revB = reverse_number(B)
        # Add them
        total = revA + revB
        # Reverse the sum and print
        print(reverse_number(str(total)))

if __name__ == "__main__":
    main()
