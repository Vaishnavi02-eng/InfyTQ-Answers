def list_of_count(word_list):
    #start writing your code here
    count_list=[]
    for i in range(0,len(word_list)):
        count_list.append(len(str(word_list[i])))
    
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))
