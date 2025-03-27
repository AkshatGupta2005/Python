x = int(input())
for i in range(1,x+1,1):
    for j in range(0,i,1):
        print("*", end="")
    print("")
# Time complexity O(N(N+1))