def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi= weight / pow(height, 2)
    print("Your BMI is " + str(round(bmi, 2)))

    if bmi < 18.5:
        print("Under Weight")
    elif bmi > 18.5 and bmi < 25:
        print("Normal Weight")
    else:
        print("Over Weight")

calculate_bmi(weight=40, height=1.73)