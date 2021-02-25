#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
  
    next_day=0
    next_month=0
    next_year=0
    if 1<=month<=12:
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if 0<day<=31:
               next_day=day+1
               next_month=month
               next_year=year
        elif month==4 or month==6 or month==9 or month==11:
            if 0<day<=30:
               next_day=day+1
               next_month=month
               next_year=year
        elif month==2:
            if 0<day<=28:
               next_day=day+1
               next_month=month
               next_year=year
        
    print(next_day,"-",next_month,"-",next_year)


generate_next_date(30,6,2015)
