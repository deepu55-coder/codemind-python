n=int(input())
t=n**2
t=str(t)
sm=0
for i in t:
 sm+=int(i)
if sm==n:
   print("Neon Number")
else:
   print("Not Neon Number")