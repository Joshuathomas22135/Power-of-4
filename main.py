# Power of 4 Check (BitWise)

n = 16

result = n & (n - 1)

if result == 0:
    if n % 3 == 1:
        print("Power of 4")
    else:
        print("Not Power of 4")