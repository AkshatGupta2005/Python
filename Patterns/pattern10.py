n = int(input())
for i in range(0, n, 1):
    for j in range(0,i,1):
        print("*", end="")
    print("")
for z in range(n,0, -1):
    for k in range(z,0,-1):
        print("*", end="")
    print("")