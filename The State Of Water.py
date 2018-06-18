temp_in_cel = int(input("Please enter the temperature in Celsius: "))
if temp_in_cel > 0 and temp_in_cel < 100:
    print("At this temperature, water is a LIQUID")
elif temp_in_cel >= 100:
    print("At this temperature, water is a GAS")
elif temp_in_cel <= 0:
    print("At this temperature, water is a SOLID")

    
    
    
