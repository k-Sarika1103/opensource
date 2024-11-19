n = int(input())
m = []
for j in range(n):
    m.append(j)
for i in range(n):
    m[i] = m[i+1]
    if((i+1)>2):
        break
print(m)
