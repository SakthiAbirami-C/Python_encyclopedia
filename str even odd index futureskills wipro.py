input1=input()
l=len(input1)
ans=[input1[0]]
if(l%2==0):
    for i in range(1,l):
        if(i%2!=0):
            ans.append(input1[i])
else:
    for i in range(1,l):
        if(i%2==0):
            ans.append(input1[i])
result="".join(ans)
print( result)