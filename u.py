N = float(input())
if N == int(N):
    print(f"int {int(N)}")
else:
    print(f"float {int(N)} {N-int(N)}")