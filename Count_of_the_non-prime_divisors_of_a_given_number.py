def isprime(a):
 if(a==1):
   return True
 for i in range(2,a):
   if(a%i==0):
      return True
 return False
n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0 and isprime(i)):
        count=count+1
print(count)