# Power of 8 Check (BitWise)

n = 64

result = n & (n - 1)

if result == 0:
    if n % 7 == 1:
        print("Power of 8")
    else:
        print("Not Power of 8")