n=int(input())
p=1
sq=n*n
temp=n
while(n!=0):
    n=n//10
    p=p*10
if(sq%p==temp):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")