n = int(input())
x = []
while(n != 0):
    a = n%10
    n = int(n/10)
    x.append(a)
print(len(x))