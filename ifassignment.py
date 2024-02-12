weight = float(input("Enter weight in kilograms:"))
height = float(input("Enter height in meters"))
bmi = weight / (height ** 2)

print(f"Your bmi is {bmi} ")

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 25:
    category = "Normalweight"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "obese"
print(f" {category}")
