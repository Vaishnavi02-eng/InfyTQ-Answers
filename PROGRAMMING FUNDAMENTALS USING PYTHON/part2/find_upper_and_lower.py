#lex_auth_0127136021907046401165

def find_upper_and_lower(sentence):
    #start writing your code here
    c=0 
    d=0
    for i in sentence:
        if i.islower():
            c+=1 
        elif i.isupper():
            d+=1
    result_list=[d,c]
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))
