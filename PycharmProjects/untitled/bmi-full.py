#bmi calculator
def info_gather():
    height = float(input("Enter the height in (inches or meters: )"))
    weight = float(input("Enter the weight in (pounds or killgrams: )"))
    unit = input("is the measurements are in Matric or Imperical ? ").lower().strip()
    return (height, weight, unit)


def cal_bmi(height, weight, unit):
    if unit == "metric":
        bmi = weight / (height ** 2)
    elif unit == "imperial":
        bmi = 703 * (weight / (height ** 2))
    print("The bmi is %s" % bmi)
    bmi_sugg(bmi)



def bmi_sugg(bmi):
    if bmi <= 18:
        print("you are under weight...please put on some mass")
    elif (bmi > 18) and (bmi <= 24):
        print("you are not over weight or under weight just perfect.")
    else:
        print("you are over weight please cut off your weight")

i=0
while i<=2:
    height, weight, unit = info_gather()
    if unit.startswith("i"):
        cal_bmi(height, weight, unit="imperial")
        #break
    elif unit.startswith("m"):
        cal_bmi(height, weight, unit="metric")
        #break
    else:
        print("enter a valid value: ")
    i += 1




