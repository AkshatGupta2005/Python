n = int(input())
for i in range(0,n+1,1):
    for j in range(97,97+i,1):
        print(str(chr(j)).upper(),end=" ")
    print("")