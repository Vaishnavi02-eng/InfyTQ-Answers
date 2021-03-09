#lex_auth_0127136008767324161169
def close_number(num1,num2,num3):
    #start writing your code here
    li=[num1,num2,num3]
    li.sort()
    if  (abs(li[0]-li[1])<=1 and abs(li[1]-li[2])>=2) or (abs(li[1]-li[2])<=1 and abs(li[1]-li[0])>=2):
        return True
    return False
    
print(close_number(6,9,6))
