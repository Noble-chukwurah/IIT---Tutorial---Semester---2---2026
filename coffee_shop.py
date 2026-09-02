# print("welcome to the python coffee shop!")
# customer_name = input("What is your name?")
# print("Hello," + customer_name + "! Let\'s order some coffee")


# price_coffee = 3.50
# price_latte = 4.00
# price_mocha = 5.00
# print("coffee: $" + str(price_coffee))
# print("Latte: $" + str(price_latte))
# print("Mocha: $" + str(price_mocha))

# while True:
#     choice = input("What would you like to order? (coffee/latte):").lower()
#     if choice == "coffee":
#         cost = price_coffee
#     elif choice == "latte":
#         cost = price_latte
#     elif choice == "mocha":
#         cost = price_mocha
#     else:
#         print("Sorry, we do not have that.")
#         continue
        
#     quantity = int(input("How many cups would you like?"))
#     order_total = cost *quantity
    
#     if quantity > 1:
#         print("You get a discount of $1.00")
#         order_total -= 1.00
    
    
#     student = input("Are you a Student? (yes/no) ")

#     if student == "yes":
#         print("Great! you will get a 10"+"%","discount")
#         order_total = order_total * 0.90


#     total_cost = total_cost + order_total
#     print("Your total is: $" + str(round((total_cost))))
#     print("Thank you" + customer_name + "! please come again.")
    

# minutes = 250

# hours = minutes // 60
# remaining_minutes = minutes % 60

# print("Hours:", hours)
# print("Minutes:", remaining_minutes)


income = float(input("What is your taxable income? "))
if income <= 20000:
    tax = 0.02 * income
elif income <= 50000:
    tax = 400 + 0.025 * (income - 20000)
else:
    tax = 1150 + 0.035 * (income - 50000)

print("Your tax is ", tax)

# menu_items = ["coffee", "latte", "expresso"]
# print("Our Menu:", menu_items)ee