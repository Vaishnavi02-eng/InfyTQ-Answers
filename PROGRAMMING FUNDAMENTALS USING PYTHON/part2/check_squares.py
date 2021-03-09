#lex_auth_0127136357122129921205

def check_squares(number):
    #start writing your code here
    for i in range(1,number):
        for j in range(1,number):
            sum=0 
            sum=(i**2)+(j**2)
            if sum==number:
                return True
    return False

number=68
print(check_squares(number))
