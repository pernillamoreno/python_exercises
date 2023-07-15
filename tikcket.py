print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  elif age >=90 and age <= 100:
    print("Sorry your dead you cant ride.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
    
  wants_a_beer = input("Do you want beer? Y or N")
  if wants_a_beer == "Y":
    amount_beer=int(input("How many? ")) 
    print(f"you want {amount_beer}")
  else:
    print("You can have water")
 
  print(f"Your final bill is ${bill} ")

else:
  print("Sorry, you have to grow taller before you can ride.")
