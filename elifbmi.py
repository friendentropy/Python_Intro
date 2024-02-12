def calculate_bmi(weight, height):
    try:
        # Convert height to meters
        height_in_meters = height / 100.0

        # Calculate BMI
        bmi = weight / (height_in_meters ** 2)

        return bmi
    except ZeroDivisionError:
        return "Error: Height cannot be zero."

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Example usage
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

result = calculate_bmi(weight, height)

if isinstance(result, float):
    print(f"Your BMI is: {result:.2f}")
    interpretation = interpret_bmi(result)
    print(f"You are classified as: {interpretation}")
else:
    print(result)
