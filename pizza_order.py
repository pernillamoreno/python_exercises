print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
small_pizza = "S"
medium_pizza = "M"
large_pizza = "L"
bill=0


#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill +=15
    print(f"It cost ${bill}.")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni == "Y":
        bill +=2
        print(f"It cost ${bill}.")
    else:
        print("Thank for your order!")    
elif size == "M":
    bill +=20
    print(f"It cost ${bill}.")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni == "Y":
        bill +=3
        print(f"It cost ${bill}.")
    else:
        print("Thank for your order!")  
else:
    bill +=25 
    print(f"It cost ${bill}.")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni == "Y":
        bill +=2
        print(f"It cost ${bill}.")
    else:
        print("ok next question.")
        
extra_cheese = input("Do you want extra cheese? Y or N ")       

if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is {bill}. Welcome back!")
else:
    print("Thanks for order. Welcome back!")
