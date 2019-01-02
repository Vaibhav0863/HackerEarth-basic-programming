t = int(input())

for l in range(t):
    data = list(map(int, input().split(" ")))
    # INPUT=> 1 44 2 14
    sh = data[0]  # 1
    sm = data[1]  # 44
    eh = data[2]  # 2
    em = data[3]  # 14

    s = (sh * 60) + sm
    e = (eh * 60) + em
    time = (e - s) / 60
    # This is used to hour ie. time[0] is worked hour by bob
    time = str(time).split(".")
    # ((60 - sm) + em)%60 is used to find worked minutes by bob
    print(time[0], ((60 - sm) + em) % 60)

'''
2 42 8 23
    hr=>min
    1 44
    S (2*60)+42=120+42=162
    E (8*60)+23=480+23=503


'''