#lex_auth_012693795044450304151
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    i=0
    total=0
    length=len(reqd_gems)
    check =  all(item in gems_list for item in reqd_gems)
    if check is True:
        while(i<length):
            inty=gems_list.index(reqd_gems[i])
            total=total+ price_list[inty]*reqd_quantity[i]
            bill_amount=total
            i=i+1
                
            if(total>30000):
                bill_amount= total - (total*5)/100
            else:
                bill_amount=total
                
    else :
        bill_amount= -1
    
    return bill_amount

gems_list=["Ivory","Jasper","Ruby","Garnet"]
price_list=[1760,2119,1599,3920,3999]
reqd_gems=["Ivory","Emerald","Garnet"]
reqd_quantity=[5,10,15]

bill_amount= calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
