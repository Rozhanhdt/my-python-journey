cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)

print("The first three items in the list are:")
print(cubes[:3])

print("Three items from the middle of the list are:")
print(cubes[4:7])

print("The last three items in the list are:")
print(cubes[-3:])
