n = int(input())
for j in range(0,n,1):
        print("*", end="")
print("")
for i in range(0,n-2,1):
    print("*", end="")
    for j in range(0,n-2,1):
        print(" ",end="")
    print("*")
for j in range(0,n,1):
        print("*", end="")
