def check_anagram(data1,data2):
    data1=data1.lower()
    data2=data2.lower()
    if(len(data1)==len(data2)):
        if(sorted(data1)!=sorted(data2)):
            return False
        else:
            if(data1[i]!=data2[i] for i in range(len(data1))):
                return True
            else:
                return False
            
    else:
        return False
            

print(check_anagram("eat","tea"))
