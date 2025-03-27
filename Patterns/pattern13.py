n = int(input())
x = 1
for i in range(0,n+1,1):
    for j in range(0,i,1):
        print(x,end=" ")
        x=x+1
    print("")