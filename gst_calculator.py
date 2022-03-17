print("Hi, Welcome to New World")
#Ask the user to enter name
name = input("Insert your name: ")
#Ask the user to input prices of the items
carrot = 2.99
apple = 3.99
#Ask the user to enter the quantity of items
num_of_carrots = int(input("Insert amount of carrots: "))
num_of_apples = int(input("Insert amount of apples: "))
#Calculate the total price of each item. (figure out the formula you need to use.)
carrot_total = carrot * num_of_carrots
apple_total = apple * num_of_apples
#Add all totals of items
total_of_items = carrot_total + apple_total
#Calculate GST (15%)
gst = 1.15
#Give the Total Price including GST
grand_total = total_of_items * gst
rounded_grand_total = round(grand_total, 2)
print("{} your order has come to: ${}".format(name,rounded_grand_total))
print("Thank you for shopping at New World")