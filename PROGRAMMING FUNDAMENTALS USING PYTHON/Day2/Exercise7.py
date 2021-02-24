#PF-Exer-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    final=0
    #Write your logic here
    Rate_per_Adult=37550.0 
    Rate_per_Child=Rate_per_Adult/3
 
    
    service_ad = (Rate_per_Adult*7)/100
    service_ch = (Rate_per_Child*7)/100
    ticket_cost1=Rate_per_Adult + service_ad 
    ticket_cost2=Rate_per_Child + service_ch
    final_cost1 = ticket_cost1-((ticket_cost1*10)/100)
    final_cost2 = ticket_cost2-((ticket_cost2*10)/100)
    cost1 = no_of_adults*final_cost1
    cost2 = no_of_children*final_cost2
    total_ticket_cost=cost1+cost2
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)
