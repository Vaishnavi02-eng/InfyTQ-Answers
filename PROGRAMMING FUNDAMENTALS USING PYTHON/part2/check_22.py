
def check_22(num_list):
    #start writing your code here
    c=0
    for i in range(0,len(num_list)-1):
        for j in range(i+1,i+2):
            if num_list[i]==num_list[j]:
               
               c+=1
    if c>=1:
        return True
    else:
        return False
print(check_22([3,2,5,1,2,1,2,2]))
