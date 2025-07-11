menu={
    'Tea':20,
    'Coffee':60,
    'Cold_coffee':90,
    'Coffee_with_icecream':130,
    'Pizza':190,
    'Pasta':240,
    'Momo':160,
    'Brownie':180,
    'Bubble_tea':250
}
#Greet
print("WELCOME TO THE CLOUD CAFE🩵")
#Menu
print("Menu Card")
print("Tea:Rs.20\nCoffee:Rs.60\nCold_coffee:Rs.90\nCoffee_with_icecream:Rs.130\nPizza:190\nPasta:240\nMomo:160\nBrownie:180\nBubble_tea:250")
order_total=0

print("Hello sir/ma'am😊")
item1=input("Enter the item1 you want to order: ")
if item1 in menu:
    order_total+=menu[item1]
    print(f"Your order {item1} has been added")
else:
    print(f"Sorry Sir/Ma'am,{item1} is not available in our cafe")
another_item=input("Sir/Ma'am, would_you_like_order_somthing(yes/no):" )
if another_item == "yes":
    item2=input("Enter the item2 you want to order: ")
    if item2 in menu:
        print(f"Your order {item2} has been added")
        order_total+=menu[item2]
    else:
        print(f"{item2}is not available")
else:
    print("Thank You Sir/Ma'am😊,Visit our cafe next time🩷.")
print(f"Your total order total is {order_total}")
print("Thank You Sir/Ma'am😊,Visit our cafe next time🩷.")