n = int(input("Enter number of stairs: "))

if n <= 2:
    print("Output:", n)
else:
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    print("Output:", b)