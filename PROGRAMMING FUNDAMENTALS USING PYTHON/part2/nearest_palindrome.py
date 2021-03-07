def nearest_palindrome(number):
    #start writitng your code here

    l=number+1000
    for i in range(number+1,l):
        temp=i
        
        rev=0
        while(i>0):
            dig=i%10
            rev=rev*10+dig
            i=i//10 
        if(temp==rev): 
            return rev
number=12300
print(nearest_palindrome(number))
