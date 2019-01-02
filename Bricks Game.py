'''
 GIVEN=>
        N number of bricks.
 TASK=>
        In this, Patlu picks i brick and Motu picks i*2 bricks

        We need to find out who will pick last brick from N number of bricks
'''


# Take input of N number of bricks

n=int(input())

# First Patlu picks i brick from N number of bricks

patlus_bricks=0
motus_bricks=0
total_bricks=0;
i=1

'''
15

1 2=15-3=12 
2 4=12-6=6
3 3=6-6=0

'''
while True:
    # Here patlu picks i brick
    if i<n:
        n=n-i
    else:
        n=0
        print("patlu")
        break

    # Here motu picks i*2 bricks
    if (i*2)<n:
        n = n -(i*2)
    else:
        n=0
        print("motu")
        break


    i+=1







