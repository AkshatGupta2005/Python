x = int(input())
for i in range(1,x+1,1):
    for j in range(1,i+1,1):
        print(i, end="")
    print("")
# Time complexity O((N+1)(N+1))