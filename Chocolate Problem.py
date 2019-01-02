''''
    *PROBLEM STATEMENT*

    Bob have N number of chocolate and Alice have M number of chocolate

    condition 1:
        if bob gives 1 to Alice then Alice have number of chocolates of * 2

    condition 2:
        if Alice gives 1 to Bob then bob have number of chocolates of alice


    Solution:
        You need to find out howmuch chocolates will alice and bob have by considering all these conditions-
'''

i=2
while True:
    #First we need to get ALice value

    Bob = i
    Alice = ((Bob - 1) * 2)
    Alice = Alice - 1


    if (Bob+1)==(Alice-1):
        print(Bob, Alice)
        break;

    i+=1
