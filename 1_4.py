print("Please enter your weight (kg): ")
a = float(input())
print("Please enter your height (meter): ")
b = float(input())
BMI = a/(b**2)
if BMI < 18.5:
    print("Underweight", "Your BMI is: ", BMI)
elif 18.5 < BMI < 24.9 :
    print("Normalweight", "Your BMI is: ", BMI)
elif 25 < BMI < 29.9 :
    print("Overweight", "Your BMI is: ", BMI)
elif 30 < BMI < 34.9 :
    print("Obesity", "Your BMI is: ", BMI)
elif 35 < BMI < 39.9 :
    print("Extreme Obesity", "Your BMI is: ", BMI)    