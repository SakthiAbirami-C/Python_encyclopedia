def create_largest_number(number_list):
    number_list.sort(reverse=True)
    largest_number = str(number_list[0])
    for i in range(0,len(number_list)-1):
        largest_number += str(number_list[i+1])
    return int(largest_number)
        
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
