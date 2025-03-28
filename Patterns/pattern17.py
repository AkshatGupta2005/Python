n = int(input())
for i in range(1,n+1,1):
    for z in range(n-i,0,-1):
        print("  ", end="")
    for j in range(0,i,1):
        print(str(chr(j+97)).upper(),end=" ")
    for k in range(i,1,-1):
        print(str(chr(k+95)).upper(),end=" ")
    print("")