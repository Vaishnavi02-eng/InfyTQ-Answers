#lex_auth_0127135787454873601143


def create_new_dictionary(prices):
    #start writing your code here
     new_dict={}
     for key in prices:
        if prices[key]>200:
            new_dict.__setitem__(key,prices[key])
   
     return new_dict

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))
