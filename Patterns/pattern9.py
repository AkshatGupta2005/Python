n = int(input())
for i in range(1,n+1,1):
    for k in range(n-i, 0, -1):
        print(" ",end="")
    for j in range(1,2*i,1):
        print("*", end="")
    print("")
for i in range(n,0,-1):
    for k in range(1,n-i+1,1):
        print(" ",end="")
    for j in range(2*i,1,-1):
        print("*", end="")
    print("")