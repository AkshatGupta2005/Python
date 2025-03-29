n = int(input())
x = []
c = 0
while(n != 0):
    a = n%10
    n = int(n/10)
    x.append(a)
for i in x:
    c = c + i*(10**len(x))
    x.pop()
print(c)