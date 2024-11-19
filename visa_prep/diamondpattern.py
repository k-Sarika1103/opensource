n = int(input())
for i in range(n):
    for j in range(i):
        print('*',end='')
    print('\t')
for k in range(n,-1,-1):
    for l in range(k):
        print('*',end='')
    print('\t')
