def cal_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = weight / (height * height)
    print("BMI = " + str(round(bmi,2)))
    if bmi < 18.5:
        print("User is underweight")
    elif bmi <= 25.0:
        print("User is normal weight")
    elif bmi > 25.0:
        print("User is overweight") 
    else:
        print("User is out of weight class")
cal_bmi( weight=80,height= 1.84)