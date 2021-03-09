#lex_auth_0127135811649044481146

def find_nine(nums):
    #Remove pass and write your code here
    c=0
    t=len(nums)
    for i in range(len(nums)-1):
	    if nums[i]==9:
	        c+=1
    
    if c>0:
        return True
    else:
        return False
nums=[1,9,4,5,6]
print(find_nine(nums))
