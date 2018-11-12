n=int(input())
f=0
for i in range(2,n//2):
    s=n%i
    if(s==0):
        f=1
        break
if f==0:
    print("yes")
else:
    print("no")
