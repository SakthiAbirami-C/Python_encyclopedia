input1=input()
input2=input()
asci=[]
count=0
for i in input1:
    asci.append(ord(i))
if(asci[0]>asci[1]):
    asci_sorted=sorted(asci,reverse=True)
else:
    asci_sorted=sorted(asci)
if(asci_sorted==asci):
    for i in range(len(input1)):
        if(input1[i]!=input2[i]):
            count+=1
    if(asci[0]>asci[1]):
        print ("Decreasing"+":"+str(count))
    else:
        print("Increasing"+":"+str(count))
else:
    print( "Invalid")