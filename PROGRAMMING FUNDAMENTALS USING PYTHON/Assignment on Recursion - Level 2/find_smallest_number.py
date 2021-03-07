
def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(1,(num+1)):
        if(num%i==0):
            factors.append(i)
    
    return factors

def find_smallest_number(num):
    i=int(1)
    
    while(True):
        
        x=find_factors(i)
        
        if(len(x)==num):
            
            break
        else:
            i=i+int(1)
    return x[-1]
    #start writing your code here

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
