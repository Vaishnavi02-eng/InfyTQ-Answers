
def check_occurence(string):
    #start writing your code here
    k=string.lower()
    k=k.split(" ")
    c=0 
    l=0 
    
    for i in k:
       
        if i=="jet":
            c+=1 
        if i=="mat":
            l+=1
    
    if c==l:
        return True
    else:
        return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))
