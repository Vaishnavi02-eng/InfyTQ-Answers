#PF-Assgn-24
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    sum=0
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    #Write your logic here
    if num3>=num2 and num3>=num1:
        if num3==(num1+num2):
            print(success)
            return success
        else:
            print(failure)
            return failure
    if num2>=num3 and num2>=num1:
        if num2==(num1+num3):
            print(success)
            return success
        else:
            print(failure)
            return failure
    if num1>=num3 and num1>=num2:
        if num1==(num3+num2):
            print(success)
            return success
        else:
            print(failure)
            return failure
    #Use the following messages to return the result wherever necessary
    
    

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)
