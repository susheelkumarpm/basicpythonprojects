name=str(input("enter your name"))
age=int(input("enter your age"))
weight=int(input("enter your weight in pounds"))
height=int(input("enter your height in inches"))
BMI=703*((weight)/(height*height))
print("your bmi is",BMI)
if BMI>0:
    if (BMI<18.5):
        print("you are underweight")
    elif(BMI<=24.9):
        print("you are normal weight")
    elif(BMI<=29.9):
        print("you are over weight")
    elif(BMI<=34.9):
        print("you are obese")
    elif(BMI<=39.9):
        print("you are severly obese")
    else:
        print("you are morbidly obese")
else:
    print("invalid input")
