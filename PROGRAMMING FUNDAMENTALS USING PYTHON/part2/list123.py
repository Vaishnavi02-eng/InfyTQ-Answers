def list123(nums):
    num = ""
    for i in nums:
        num += str(i)
    if "123" in num:
        return True
    else:
        return False
        
nums=[1,2,3,4,5]
print(list123(nums))
