n = int(input())
c = 0
negative = False
if(n <0):
    negative = True
    n = 0 - n
if(n < 2**31 and n > -(2**31)):
    while (n != 0):
        a = n%10
        n = int(n/10)
        c = (c*10) + a
if(n < 2**31 and n > -(2**31)):       
    if(negative == True):
        print(0 - c)
    else:
        print(c)
else:
    print(0)