n,m = map(int,input().split())
k = []
for j in range(n):
    k.append(j)
num1=0
num2=0
for i in k:
    if(k[i]%m!=0):
        num1=num1+k[i]
    else:
        num2=num2+k[i]
print(num1-num2)
