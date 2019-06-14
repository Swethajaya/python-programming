n=input()
sd=input()
n=str(n)
sd=str(sd)
l=[]
x=[]
for i in n:
  l.append(i)
  l.sort(reverse=True)
print(l)
print(sd)
ll=len(l)-1
for i in sd:
  x.append(l[ll-i])
for i in x:
  print(i,end="")
