#lex_auth_0127136084107673601177

def rotate_list(input_list,n):
    #start writing your code here
    k=input_list[::-1]
    l=k[0:n]
    l=l[::-1]
    output_list=l+input_list[0:len(input_list)-n]
    return output_list

input_list= [10,20,30,40,50]
output_list=rotate_list(input_list,2)
print(output_list)
