m=int(input())
n=int(input())
v=[]
same=list(map(int,input().split()))
for i in range(1,m+1):
    v.append(i)
    if i in same:
        v.remove(i)
sum=0
l=[]
s=[]
for i in v:
    if(sum+i <m):
        l.append(i)
        sum+=i
    else:
        s.append(len(l))
        l.clear()

print(max(s))