N = int(input())

years = N // 365
N %= 365

months = N // 30
N %= 30

days = N

print(years, "years")
print(months, "months")
print(days, "days")
