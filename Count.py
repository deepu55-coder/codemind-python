n=int(input())
e=0
o=0
arr=[int(i)for i in input().split()]
for i in range(len(arr)):
    if(arr[i]%2==0):
        e+=1
    else:
        o+=1
print(e,o)        