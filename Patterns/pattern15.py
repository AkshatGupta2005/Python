n = int(input())
for i in range(n,0,-1):
    for j in range(97, 97+i,1):
        print(str(chr(j)).upper(),end="")
    print("")