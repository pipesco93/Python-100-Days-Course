# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters e.g., 1.55: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms e.g., 72: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight/(height * height)

print(f"Height ${height} m")
print(f"Weight ${height} kg")

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
