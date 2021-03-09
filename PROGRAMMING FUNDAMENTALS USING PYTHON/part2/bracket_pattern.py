#lex_auth_0127135773590405121141

def bracket_pattern(input_str):
    #Remove pass and write your code here
    c=m=0
    l=list(str(input_str))
    for i in range(len(l)):
        if input_str.startswith("("):
            if l[i]=="(":
               c+=1
            if l[i]==")":
               m+=1
        else:
            return False
    if c==m:
        return True
    else:
        return False

    
input_str="(())("
print(bracket_pattern(input_str))
