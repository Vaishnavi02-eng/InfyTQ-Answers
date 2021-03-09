#lex_auth_0127136251125350401190

def divisible_by_sum(number):
    #start writing your code here
    temp=number
    k=len(str(number))
    sum=0
    while k>0:
        sum+=number%10 
        number=number//10 
        k-=1
    if(temp%sum==0):
        return True
    else:
        return False
number=25
print(divisible_by_sum(number))
