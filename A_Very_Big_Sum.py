n=int(input())
sum=0
arr=[int(i) for i in input().split()]
for i in range(len(arr)):
    sum=sum+arr[i]
print(sum)