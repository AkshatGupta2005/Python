n = int(input())
for i in range(0,n,1):
    x = n
    for k in range(0,i,1):
        x=x-1
        for j in range(0,n,1):
            print(x,end="")

    print("")