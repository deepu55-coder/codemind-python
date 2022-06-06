n=int(input())
m=int(input())
c=0;
s=0;
for i in range(1,n):
    if(n%i==0):
        c=c+i;
for i in range(1,m):
    if(m%i==0):
        s=s+i
if(c==m and s==n):
    print("Amicable")
else:
    print("Not Amicable")