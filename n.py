# Read the input character
ch = input().strip()

# If the character is lowercase, print its uppercase version
if ch.islower():
    print(ch.upper())
# If the character is uppercase, print its lowercase version
else:
    print(ch.lower())