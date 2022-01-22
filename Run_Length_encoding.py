def encode(message):
    result=""
    current_run_char=""
    previous_run_char=""
    run_length=0
    
    for i in range(0,len(message)):
        
        if i==0:
            current_run_char=message[i]
            run_length=1
        elif(i!=0):
            current_run= message[i]
            if current_run==current_run_char:
                run_length +=1
            else:
                result += str(run_length)+current_run_char
                current_run_char=current_run
                run_length=1
    
    result += str(run_length)+current_run_char
               
    return result 

encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
