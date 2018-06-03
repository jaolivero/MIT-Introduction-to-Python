
r = 0.04
portion_down_payment = 0.25
current_savings = 0.0


annual_salary = float(input( "What is your annual salary: "))
portion_saved = float(input("what percentage of your salary would you like to save? write as a decimal: "))
total_cost = float(input("what is the cost of your deam home: "))

monthly_savings = (annual_salary / 12) * portion_saved
down_payment = total_cost * portion_down_payment
months = 0

while current_savings < down_payment:
                     
                      current_savings += monthly_savings + (current_savings * r / 12)
                      months += 1
                    
                      
print ("It would take you " + str(months) + " months to save for the down payment of your dreams home")
print(months)
