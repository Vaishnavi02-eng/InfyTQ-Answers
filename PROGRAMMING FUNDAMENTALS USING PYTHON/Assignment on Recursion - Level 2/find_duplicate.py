def find_duplicates(list_of_numbers):
    d=[]
    
    for i in range(0,len(list_of_numbers)):
        c=0
        for j in range(0,len(list_of_numbers)):
            
            if list_of_numbers[i]==list_of_numbers[j]:
                c+=1
                if c>=2:
                   d.append(list_of_numbers[i])
    list_set=set(d)
    return list(list_set)    
    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
