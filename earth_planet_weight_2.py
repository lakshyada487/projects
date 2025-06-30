earth_weight = float(input("Earth weight: "))
planet_number = int(input("Planet number (1-7): "))
destination_weight = 0.0
if planet_number == 1:
   destination_weight = earth_weight * 0.38
elif planet_number == 2:
    destination_weight = earth_weight * 0.91
elif planet_number == 3:
    destination_weight = earth_weight * 0.38
elif planet_number == 4:
    destination_weight = earth_weight * 2.53
elif planet_number == 5:
    destination_weight = earth_weight * 1.07
elif planet_number == 6:
    destination_weight = earth_weight * 0.89
elif planet_number == 7:
    destination_weight = earth_weight * 1.14
else:
    print("Invalid planet number.")
print("your destination weight is ", destination_weight)
