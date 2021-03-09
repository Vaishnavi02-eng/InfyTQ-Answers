
def check_numbers(num1,num2):
    #start writing your code here
    
    num_list=[]
    for i in range(num1,(num2//2)+1):
        for x in range(i+1,num2+1):
            if x%i==0:
                num_list.append(x)
                 
            #num_list.append(i)
    #print(l) 
    num_list=set(num_list)
    count=len(num_list)
    return [num_list,count]

num1=2
num2=20
print(check_numbers(num1, num2))
