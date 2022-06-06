n=int(input())
p=1;
s=0;
while n>0:
    d=n%10;
    n=n//10;
    p=p*d;
    s=s+d;
print(p-s)