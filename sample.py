import random
data=list(map(int,input().split(" ")))
a,b,c=data

cnt=0
cnt1=0
for i in range(a+1):
      for j in range(b+1):

            if (i+j)<c:
                  cnt+=1

print(str(cnt)+"/"+str(a+1))