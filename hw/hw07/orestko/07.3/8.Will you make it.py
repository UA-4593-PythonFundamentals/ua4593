def reach_gas(distance, miles, gallons):
    return miles * gallons >= distance


print(reach_gas(50, 25, 2))
print(reach_gas(60, 25, 2))