aaa = [ 50, 60, 4, 45, 55, 20]
#print(Pype(aaa),end="\n\n")
for BMI in aaa:
    if BMI < 18.5:
        bmi_index = '體重過輕'
    elif 18.5 <= BMI < 24.0:
        bmi_index = '正常範圍'
    elif 24.0 <= BMI < 27.0:
        bmi_index = '體重過重'
    elif 27.0 <= BMI < 30.0:  
        bmi_index = '輕度肥胖'
    elif 30.0 <= BMI < 35.0:
        bmi_index = '中度肥胖'
    else:
        bmi_index = '重度肥胖'
    print("BMI =",BMI,"==>",bmi_index)