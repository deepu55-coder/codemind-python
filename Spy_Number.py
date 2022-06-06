n=int(input())
sum=0
m=1
temp=n
while(temp!=0):
    d=temp%10
    sum=sum+d
    m=m*d
    temp=temp//10
if(sum==m):
    print('Spy Number')
else:
    print('Not Spy Number')
    