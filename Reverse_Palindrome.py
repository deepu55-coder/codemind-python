def fun(n):
    rev=0
    temp=n
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    r=temp+rev
    t=r
    res=0
    while r>0:
        p=r%10
        res=res*10+p
        r=r//10
    if(res==t):
        return res
    else:
        return fun(t)
n=int(input())
print(fun(n))