def half_diamond(n):
    for i in range(1, n + 1):
        print("*" + str(i) * i + "*")
    for i in range(n - 1, 0, -1):
        print("*" + str(i) * i + "*")

half_diamond(5)