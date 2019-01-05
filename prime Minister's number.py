data=list(map(int,input().split(" ")))
a,b=data
result=""
for i in range(a,b+1):
    cnt=0
    for l in range(1,i+1):
        if i%l==0:
            cnt+=1
    if cnt==2:
        x,y=list(map(int,str(i)))
        cnt1=0
        for t in range(1,(x+y)+1):
            if (x+y)%t==0:
                cnt1+=1
        if cnt1==2:
            result+=(str(x)+str(y))+" "
print(result)