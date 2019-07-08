w= int(input())
s=[]
for i in range(0,w):
 lan=input()
 s.append(lan)
l=[]
for i in zip(*s):
 if(i.count(i[0])==len(i)):
  l.append(i[0])
 

print(''.join(l))
