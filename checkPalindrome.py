n = int(input())
m = n
a = 0
mid = int(len(str(n))/2)
while(mid != 0):
    a = (m%10) + (a*10)
    m = int(m/10)
    mid = mid-1
if(len(str(n))%2 != 0):
    a = (m%10) + (a*10)
if(a == m):
    print("Palindrome Number")
else:
    print("Not Palindrome")