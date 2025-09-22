print("Reduce the waste and save our Earth")
print("Welcoming you to save our environment")

total_money = 0

# Membership card check
membership = input("Do you have a membership card (yes/no): ").strip().lower()
if membership == "yes":
    total_money += 200
else:
    total_money = 0

print("Choose the material of waste you are disposing ")
print("1. Cardboard")
print("2. Aluminium")
print("3. Plastic")
print("4. Glass Bottles")
print("5. Exit")

while True:
    ch = int(input("Enter your Choice (1-5): "))

    if ch == 1:
        wei = float(input("Enter the weight of cardboard (in kg): "))
        res = wei * 15
        print("The amount of money you will receive (in Rs):", res)
        total_money += res

    elif ch == 2:
        wei = float(input("Enter the weight of Aluminium (in kg): "))
        res = wei * 99
        print("The amount of money you will receive (in Rs):", res)
        total_money += res

    elif ch == 3:
        wei = float(input("Enter the weight of Plastic (in kg): "))
        res = wei * 30
        print("The amount of money you will receive (in Rs):", res)
        total_money += res

    elif ch == 4:
        wei = float(input("Enter the weight of Glass Bottles (in kg): "))
        res = wei * 25
        print("The amount of money you will receive (in Rs):", res)
        total_money += res

    elif ch == 5:
        print("Total money you will receive (in Rs):", total_money)
        break

    else:
        print("Invalid Choice, Try again")

# Money transfer
print("To receive the amount")
mobile = input("Enter your 10-digit mobile number linked to bank account: ")
if mobile.isdigit() and len(mobile) == 10:
    print(f"You will receive {total_money} Rs from our website.")
else:
    print("Invalid input. Please enter a valid 10-digit mobile number.")

# Membership creation
print("To create a membership card")
create = input("Are you interested to create a membership card? (yes/no): ").strip().lower()
if create == "yes":
    name = input("Enter your name: ")
    address = input("Enter your residential address: ")
    gender = input("Enter your gender: ")
    mobile_new = input("Enter your mobile number: ")
    print("You will receive a membership card from our website.")
elif create == "no":
    print("Thank you for using our application")
else:
    print("Invalid input. Please enter a valid input")

# Rating system
print("Rate us")
rate = input("Are you interested to rate us? (yes/no): ").strip().lower()
if rate == "yes":
    print("Choose a number to rate us")
    print("1. Outstanding")
    print("2. Very good")
    print("3. Good")
    print("4. Satisfactory")
    print("5. Disappointing")
    
    ch = int(input("Enter your choice: "))
    if ch == 1:
        print("Your idea is outstanding")
    elif ch == 2:
        print("Your idea is very good")
    elif ch == 3:
        print("Your idea is good")
    elif ch == 4:
        print("Your idea is satisfactory")
    elif ch == 5:
        print("Your idea is disappointing")
    else:
        print("Invalid input. Please enter a valid input")
elif rate == "no":
    print("Exit")
    print("Thank you for using our application")
    print("Welcoming you for next time")
else:
    print("Invalid input. Please enter valid input")

# Feedback
feedback = input("Enter your feedback or suggestion: ")
print("Thank you for your feedback:", feedback)
