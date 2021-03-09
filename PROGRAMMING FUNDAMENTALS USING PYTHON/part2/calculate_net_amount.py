#lex_auth_0127135929511936001157

def calculate_net_amount(trans_list):
    #start writing your code here
    dip=0 
    wit=0
    net_amount=0
    for i in range(len(trans_list)):
        c=trans_list[i].split(":")
        if c[0]=="D":
            dip+=int(c[1])
        else:
            wit+=int(c[1])
    net_amount=dip-wit        
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
