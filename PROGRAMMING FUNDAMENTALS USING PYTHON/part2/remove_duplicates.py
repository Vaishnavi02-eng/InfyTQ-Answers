def remove_duplicates(value):
    l1=list(value)
    l=[]
    str=''
    for i in range(0,len(l1)):
        for j in range(0,len(l1)):
            if not(l1[j] in l):
               l.append(l1[j])
    for Do in l:
        str+=Do
    return str
    #start writing your code here

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
