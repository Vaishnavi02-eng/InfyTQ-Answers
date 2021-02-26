#PF-Exer-15

def find_sum_of_digits(number):
    sum_of_digits=0
    #Write your logic here
    r1=0
    r2=0
    r3=0
    r1=number%10
    number=number/10
    r2=number%10
    number=number/10
    r3=number%10
    number=number/10
    sum_of_digits=int(r1+r2+r3)
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
                                          
