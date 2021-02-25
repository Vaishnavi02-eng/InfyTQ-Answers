#PF-Exer-11

def display(num):
    message=""
    #write your logic here
    if num%3==0 and num%5==0:
        print("Zoom")
    elif num%3==0:
        print("Zip")
    elif num%5==0:
        print("Zap")
    else:
        print("Invalid")
    return message

#Provide different values for num and test your program
message=display(9)
print(message)
