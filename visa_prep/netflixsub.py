a,b,c,x = map(int,input().split())
if(x<=a+b or x<=b+c or x<=a+c):
    print("YES")
else:
    print("NO")
