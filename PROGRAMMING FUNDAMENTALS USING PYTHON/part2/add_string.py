
def add_string(str1):
  #start writing your code here
  k=len(str1)
  if k>2:
    if str1.endswith("ing"):
        l=str1+"ly"
        return l
    else:
        l=str1+"ing"
        return l
  else:
      return str1

str1="com"
print(add_string(str1))
