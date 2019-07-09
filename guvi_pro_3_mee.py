a,b=input().split()
l1=len(a)
l2=len(b)
w=abs(len(a)-len(b))

#m=max(l1,l2)
for i in range(0,l1):
  if a[i]!=b[i]:
    w=w+1
print(w) 
