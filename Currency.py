# Avasthi's Notes Problem using match-case (Python 3.10+)

amount = int(input("Enter the total amount: "))

# Copy the original amount for display (optional)
remaining_amount = amount

print("\nBreakdown of notes:")

# Loop through each denomination
for denom in [100, 50, 20, 10, 5, 2, 1]:
    if denom == 100:
        notes = amount // 100
        amount %= 100
        print("100 Rs notes:", notes)
    elif denom == 50:
        notes = amount // 50
        amount %= 50
        print("50 Rs notes:", notes)
    elif denom == 20:
        notes = amount // 20
        amount %= 20
        print("20 Rs notes:", notes)
    elif denom == 10:
        notes = amount // 10
        amount %= 10
        print("10 Rs notes:", notes)
    elif denom == 5:
        notes = amount // 5
        amount %= 5
        print("5 Rs notes:", notes)
    elif denom == 2:
        notes = amount // 2
        amount %= 2
        print("2 Rs notes:", notes)
    elif denom == 1:
        notes = amount // 1
        amount %= 1500
        print("1 Rs notes:", notes)

print(f"\nTotal amount verified: ₹{remaining_amount}")
