#Bai 2
print("====BMI CALCULATOR====")
while True:
    print("")
    print("Enter your height \(inches): ")
    height = float(input())
    print("Enter your weight \(pounds): ")
    weight = float(input())
    bmi = round((weight/height**2),2)
    print("====RESULT====")
    print("YOUR BMI IS", bmi)
    if bmi < 18.5:
        print("UNDERWEIGHT")
    elif bmi >= 18.5 and bmi < 25.0:
        print("NORMAL")
    elif bmi >= 25.0 and bmi < 30.0:
        print("OVERWEIGHT")
    else:
        print("OBESE")