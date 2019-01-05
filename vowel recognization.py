t=int(input())

for n in range(t):
    string = input()
    # baceb

    cnt = 0
    # string[starting:ending]
    for i in range(0, len(string)):
        for j in range(i + 1, len(string) + 1):
            for l in string[i:j]:
                if l in 'aeiouAEIOU':
                    cnt += 1
    print(cnt)