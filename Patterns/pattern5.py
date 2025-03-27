x = int(input())
for i in range(x,0,-1):
    for j in range(i,0,-1):
        print("*", end="")
    print("")
# Time complexity O(N^2)