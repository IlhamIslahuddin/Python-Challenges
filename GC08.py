def calc_bmi():
    status = ""
    weight = float(input("Input your weight in kilograms: "))
    height = float(input("Input your height in meters: "))
    bmi = weight/(height**2)
    if bmi < 18.5:
        status = "Underweight"
    elif bmi >= 25 and bmi < 30:
        status = "Overweight"
    elif bmi >= 30:
        status = "Obese"
    else:
        status = "Normal"
    print ("Your BMI (Body Mass Index) is ",bmi,"\n Your BMI status is ",status)

if __name__ == "__main__":
    calc_bmi()
