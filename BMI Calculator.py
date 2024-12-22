def check_bmi():
    """Function to check BMI"""

    if (bmi >= 40.0):
        print(f"Your category according to BMI range is Obesity Class III")

    elif (bmi >= 35.0):
        print(f"Your category according to BMI range is Obesity Class II")

    elif (bmi >= 30.0):
        print(f"Your category according to BMI range is Obesity Class I")

    elif (bmi >= 25.0):
        print(f"Your category according to BMI range is Overweight")

    elif (bmi >= 18.5):
        print(f"Your category according to BMI range is Normal Weight")

    else:
        print(f"Your category according to BMI range is Underweight.")



# Taking Height and Weight as input.

weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))


bmi = weight / (height ** 2)
print(f"Your BMI index is {bmi}.")

print(check_bmi())     # Calling the check_bmi function.

