##inputs we need from user
#total rent of the room
#total food ordered
#total units of electricity spend
#charge per units
#total bill for electricity
#no of people living in the room
##final output

rent = int(input("enter the total rent of the room: "))
food = int(input("enter the cost of food ordered: "))
electricity = int(input("enter the units of electricity used: "))
charge_per_unit = int(input("enter the charge per unit: "))
total_people = int(input("enter the number of people: "))

total_bill = electricity * charge_per_unit

output = (rent + food total_bill) // total_people
               