import decimal
x = input('Enter your weight in kilograms:')
y = input('Enter your height in meters:')
d = decimal.Decimal(y) * decimal.Decimal(y)
print("Your BMI is",(int (x) /(d)))
if (int (x) /(d)< 18.5):
    print("You are underweight, try to increase your weight to achieve a BMI of 18.5 or greater!")
else:
    if (int (x) /(d)> 24.9):
        print("Your BMI is above a healthy amount, try to reduce your weight to achieve a BMI of 24.9 or less.")
    else:
        print("Your BMI is healthy! Try to keep it that way!")
