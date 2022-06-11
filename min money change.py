s=int(input())
def value(s):
    result=0
    if(s>=100):
        rem=s%100
        result+=s//100
        if(rem==0):
            result=s/100
    elif(s>=50):
        rem=s%50
        result+=s//50
        if(rem==0):
            result=s/50
    elif(s>=10):
        rem=s%10
        result+=s//10
        if(rem==0):
            result=s/10
    elif(s>=5):
        rem=s%5
        result+=s//5
        if(rem==0):
            result=s/5
    elif(s>=2):
        rem=s%2
        result+=s//2
        if(rem==0):
            result=s/2
    else:
        rem=s
        result=s
    return remainder1(rem,result)

def remainder1(rem,result):
    if(rem>=50):
        result+=rem//50
        rem=rem%50
        return remainder1(rem,result)
    elif(rem>=10):
        result+=rem//10
        rem=rem%10
        return remainder1(rem,result)
    elif(rem>=5):
        result+=rem//5
        rem=rem%5
        return remainder1(rem,result)
    elif(rem>=2):
        result+=rem//2
        rem=rem%2
        return remainder1(rem,result)
    elif(rem>=1):
        result+=rem
        return result
    else:
        result=result
        return result

ans=value(s)
print(int(ans))   



