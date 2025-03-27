n = int(input())
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(j,end="")
    for z in range(2*(n-i), 0, -1):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k,end="")
    print("")