n = int(input())
for i in range(n,0,-1):
    for j in range(i-1,n,1):
        print(str(chr(j+97)).upper(),end=" ")
    print("")