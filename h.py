import math

A, B = map(int, input().split())

floor_result = A // B
ceil_result = math.ceil(A / B)

# Standard rounding (0.5 and above goes up)
value = A / B
round_result = int(value + 0.5)

print(f"floor {A} / {B} = {floor_result}")
print(f"ceil {A} / {B} = {ceil_result}")
print(f"round {A} / {B} = {round_result}")
