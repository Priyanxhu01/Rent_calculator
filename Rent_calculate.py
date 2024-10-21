# Inputs we need from the user
# Total rent
# Total food ordered 
# Electricity units spend
# Charge per unit 
# Persons living in room

## Output 
# Total amount you've to pay is


rent = int(input(" Enter your hostel/flat rent = "))
food = int(input(" Enter the amount of food ordered = "))
electricity_spend = int(input(" Enter the total of electricity units spend = "))
charge_per_unit = int(input(" Enter the charge per unit = "))
person = int(input(" Enter the number of person living in room/flat = "))

total_amount = rent + food + electricity_spend * charge_per_unit 

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // person

print(" Total_amount : ",total_amount)
print(" Total_bill : ",total_bill)
print(" Each person will pay :",output)




