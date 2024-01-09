weight = float(input("Weight:"))
unit=input("(L)bs or (K)g:")
if unit.upper()=="L":
    convertedWeight = weight * 0.45
    print(f"You are {convertedWeight} kilos!")
elif unit.upper()=="K":
    convertedWeight = weight / 0.45
    print(f"You are {convertedWeight} pounds!")