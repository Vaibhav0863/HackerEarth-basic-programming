def solve(A, B, n):
    if B[0] <= A[-1]:
        return 0
        
    monki = 0
    i = 0
    for j in range(n):
        if j >= i and B[j] >= A[i]:
            monki = max(monki, j - i)
        else:
            i+=1
            if i == n:
                break
    return monki
 
for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solve(A, B, n))