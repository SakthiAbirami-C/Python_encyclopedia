#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    sum=0
    
    for i in chocolates_received:
        sum +=i
    return sum
    

def reward_child(child_id_rewarded,extra_chocolates):
    
    if(extra_chocolates<1):
        print("Extra chocolates is less than 1")
    elif(child_id_rewarded not in child_id):
        print("Child id is invalid")
    else:
        for num in range(0,len(child_id)):
            if child_id[num]==child_id_rewarded:
                chocolates_received[num]=chocolates_received[num]+extra_chocolates
        print(chocolates_received)
             

    
    


print(calculate_total_chocolates())
reward_child(20,2)
