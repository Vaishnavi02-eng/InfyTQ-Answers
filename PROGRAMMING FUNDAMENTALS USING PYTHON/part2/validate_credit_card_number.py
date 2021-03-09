#lex_auth_01269445968039936095

def validate_credit_card_number(card_number):
    #start writing your code here
    l=[]
    card_no_list=[]
    card_no_list=list(str(card_number))
    if len(card_no_list)==16:
        i=len(card_no_list)-2
        while(i>=0):
            l.append(int(card_no_list[i])*2)
            i-=2
        for i in range(0,len(l)):
            if l[i]>9:
                sum=0
                t=len(str(l[i]))  
                while l[i]>0:
                    sum+=l[i]%10
                    l[i]=l[i]//10
                l[i]=sum
        sum=0
        for i in range(0,len(l)):
            sum+=int(l[i])
        i=len(card_no_list)-1
        while(i>=0):
            sum+=int(card_no_list[i])
            i-=2
        
        if sum%10==0:
            return True
        else:
            return False

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
