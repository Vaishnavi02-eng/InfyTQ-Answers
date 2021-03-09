#lex_auth_0127135945621340161163

def string_both_ends(input_string):
	#start writing your code here
	k=len(str(input_string))
	st=''
	if k==2:
	    st=input_string+input_string
	    return st
	elif k>2:
	    st=input_string[0:2]+input_string[-2:]
	    return st
	if k==1:
	    return -1

input_string="w3w"
print(string_both_ends(input_string)) 
