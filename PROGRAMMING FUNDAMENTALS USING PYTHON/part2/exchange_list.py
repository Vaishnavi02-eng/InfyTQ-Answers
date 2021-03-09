#lex_auth_0127136357873991681201

def exchange_list(number_list):
    #start writing your code here
    
    k=int(len(number_list)/2)
    d=number_list[k::]
    s=number_list[0:k]
    m=d[::-1]+s
    
    return m
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))
