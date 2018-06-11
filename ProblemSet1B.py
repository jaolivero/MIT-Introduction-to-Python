r = 0.04
current_savings = 0
portion_down_payment = 0.25

annual_salary = int(input("What is your annual salary?: "))
portion_saved = float(input("Write the percent of your salary to save, as a decimal: "))
total_cost = int(input("What is the total cost of your dream home?: "))
semi_annual_raise = float(input("What is your annual six month raise? as a decimal: "))

monthly_savings = (annual_salary / 12) * portion_saved
down_payment = total_cost * portion_down_payment
months = 0

while current_savings < down_payment:
    current_savings += monthly_savings + (current_savings * r / 12)
    months += 1

    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_savings = (annual_salary / 12.0) * portion_saved


print ("It would take you " + str(months) + " months to save for the down payment of your dreams home")
