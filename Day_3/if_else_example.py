print("Welcome to de rollercoaster!")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride!")
    age = int(input("Wha is your age? "))

    if age < 12:
        bill = 5
        print(f"Child tickets are  ${bill}")
    elif age <= 18:
        bill = 7
        print("Youth tickets are ${bill}")
    else:
        bill = 12
        print("Adult tickets are ${bill}")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3
    print(f"You pay ${bill}")
   

else:
    print("Sorry, you can't ride")