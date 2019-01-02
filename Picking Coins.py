t=int(input())

for i in range(1,t+1):
    data = input()

    data = data.split(" ")

    data[0] = int(data[0])

    data[1] = int(data[1])

    i = 1;
    if data[1]==1:
        if data[0]%2==0:
            print("Bob")
        else:
            print("Alice")
    else:
        while True:
            # first Alice remove number of k for given coins
            if data[1] <= data[0]:
                data[0] = data[0] - (data[1])

            else:
                print("Bob")
                break
            # Second Bob remove k numbers coins from total
            if data[1] <= data[0]:
                data[0] = data[0] - (data[1])

            else:
                print("Alice")
                break

            i = i + 1
            data[1] = data[1]**i



