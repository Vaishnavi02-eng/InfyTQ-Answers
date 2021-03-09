import re
def validate_name(name):
    #Start writing your code here
    if len(name)<=15 and name.isalpha() and not(name==" "):
        
        return True
    else:
        return False

def validate_phone_no(phno):
    #Start writing your code here
    phnoset=list(set([i for i in phno]))
    if len(phno)==10 and phno.isdigit() and len(list(phnoset))!=1:
        
        return True
        
    else:
        return False

def validate_email_id(email_id):
    #Start writing your code here
    if re.match(r"\w+@(gmail|yahoo|hotmail)\.com",email_id):
        return True
    else:
        return False

def validate_all(name,phone_no,email_id):
    k=0
    if(validate_name(name)==False):
        print("Invalid Name")
    else:
        k+=1
    if(validate_phone_no(phone_no)==False):
        print("Invalid phone number")
    else:
        k+=1
    if(validate_email_id(email_id)==False):
        print("Invalid email id")
    else:
        k+=1
    if k==3:
        print("All the details are valid")
        
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")
