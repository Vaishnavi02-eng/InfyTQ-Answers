def count_digits_letters(sentence):
    count=0
    num=0
    for i in sentence:
        if i.isalpha():
            count+=1
        elif i.isnumeric():
            num+=1
    return [count,num]
sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
