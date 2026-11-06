High_sales_limit = 15000.00
Mid_sales_limit = 10000.00
Min_sales_limit = 0.00 

High_Rate = 0.09
Mid_Rate = 0.065
Min_Rate = 0.04

try:
    gross_sales = float(input('please enter the gross sales for this salesperson: $'))
except:
    print("")

if gross_sales < Min_sales_limit:
    print("sorry, the gross sales amount cannot be negative. Ending the program.")
else:

    if gross_sales > High_sales_limit:
        commission_rate = High_Rate 
    elif gross_sales > Mid_sales_limit:
        commission_rate = Mid_Rate
    else:
        commission_rate = Min_Rate

    Commission_amount = gross_sales * commission_rate
    print('This salesperson\'s commission is $' + str(round(Commission_amount, 2)))

input('\nPress Enter to exit the program...')

