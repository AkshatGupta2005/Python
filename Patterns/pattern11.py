n = int(input())
for i in range(1,n+1,1):
    for j in range(i,0,-1):
        if(j%2 == 0):
            print("0",end="")
        else:
            print("1", end="")
    print("")