t=int(input())

for l in range(0,t):
    i = int(input())

    if i % 12 == 0:
        print(i - 11, "WS")
    elif i % 12 == 1:
        print(i + 11, "WS")
    elif i % 12 == 2:
        print(i + 9, "MS")
    elif i % 12 == 11:
        print(i - 9, "MS")
    elif i % 12 == 3:
        print(i + 7, "AS")
    elif i % 12 == 10:
        print(i - 7, "AS")
    elif i % 12 == 4:
        print(i + 5, "AS")
    elif i % 12 == 9:
        print(i - 5, "AS")
    elif i % 12 == 5:
        print(i + 3, "MS")
    elif i % 12 == 8:
        print(i - 3, "MS")
    elif i % 12 == 6:
        print(i + 1, "WS")
    elif i % 12 == 7:
        print(i - 1, "WS")