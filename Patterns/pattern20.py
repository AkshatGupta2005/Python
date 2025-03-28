n = int(input())
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print("*", end="")
    for j  in range((n-i)*2-1,1, -1):
        print(" ",end="")
    for j in range(0,i+1,1):
        print("*", end="")
    print("")
for i in range(n-1,0,-1):
    for j in range(0,i,1):
        print("*", end="")
    for j  in range(0, (n-i)*2, 1):
        print(" ",end="")
    for j in range(0,i,1):
        print("*", end="")
    print("")
