string=input()
x=0
y=0

for c in string:
    if c=='L':
        x=x-1
    elif c=='R':
        x=x+1
    elif c=='U':
        y=y+1
    else:
        y=y-1

print(x,y)
