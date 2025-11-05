def cal_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = weight / (height * height)
    print("BMI = " + str(round(bmi,2)))
    if bmi < 18.5:
       return -1
    elif bmi <= 25.0:
       return 0
    elif bmi > 25.0:
        return 1
    else:
        print("User is out of weight class")
cal_bmi( weight=80,height= 1.84)