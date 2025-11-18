A, S, B, _, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if S == '+':
    result = A + B
elif S == '-':
    result = A - B
else:
    result = A * B
print("Yes" if result == C else result)