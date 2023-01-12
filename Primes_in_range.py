import math
def isprime(n):
    sq=int(math.sqrt(n))
    if(n==1):
        return 0
    else:
        for i in range(2,sq+1):
            if(n%i==0):
                return 0
                break
    return 1
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if(isprime(i)==1):
        c+=1
print(c)