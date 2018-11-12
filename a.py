n=int(input())
s=0
n1=n
while n>0:
  r=n%10
  s=s*10+r
  n=n//10
if(n1==s):  
  print("YES")
else:
  print("NO")
  
  
