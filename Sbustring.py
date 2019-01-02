import math

t=int(input())

for p in range(0,t):

    m=input()
    string = input()

    if len(string)==1:
        print("1")
    else:
        max_string_len = 0;
        for i in range(0,len(string)):
            j=len(string)+1
            for l in range(j,i+2,-1):
                #print(string[i:j])

                #here we find out substring of given substring
                str = string[i:j]

                half_str=len(str)//2

                #we need to create list of given substring



                for l in str:
                    if str.count(l)>=half_str:
                        temp=len(str)

                        if max_string_len<temp:
                            max_string_len=temp
                        break


        print(max_string_len)