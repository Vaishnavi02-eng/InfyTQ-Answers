def seed_no(number,ref_no):
    #start writing your code here
    if ref_no%number==0:
        return True 
    else:
        return False
number=123
ref_no=738
print(seed_no(number,ref_no))
