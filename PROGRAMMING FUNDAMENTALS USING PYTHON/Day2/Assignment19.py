#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if food_type=="N":
        if distance_in_kms<=3:
           bill_amount=quantity_ordered*150+0
        elif distance_in_kms>3 and distance_in_kms<=6:
           bill_amount=quantity_ordered*150+3
        else:
           bill_amount=quantity_ordered*150+6 
    elif food_type=="V":
        if distance_in_kms<=3:
           bill_amount=quantity_ordered*120+0
        elif distance_in_kms>3 and distance_in_kms<=6:
           bill_amount=quantity_ordered*120+3
        else:
           bill_amount=quantity_ordered*120+6       
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
