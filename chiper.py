'''
    here a => 97 and z=>122

    if ord(c)+k>25:
        chr(25-ord(c)+0)

    // x=1/26+res
'''
import math
string=input()
k=int(input())

result=""

for c in string:
    if ord(c)>=97 and ord(c)<=122:
        ch = ord(c) + k - 97
        ch = ch % 26
        result=result+chr(ch+97)
    elif ord(c)>=65 and ord(c)<=90:
        ch = ord(c) + k - 65
        ch = ch % 26
        result = result + chr(ch + 65)
    elif ord(c)>=48 and ord(c)<=57:
        ch = ord(c) + k - 48
        ch = ch % 10
        result = result + chr(ch + 48)
    else:
        result=result+c
print(result)