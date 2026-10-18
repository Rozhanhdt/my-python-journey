million = list(range(1, 1_000_001))
odd_numbers = list(range(1, 21, 2))
threes = list(range(3, 31, 3))

cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)

cubes_comprehension = [number ** 3 for number in range(1, 11)]

print("Counting to twenty:")
for number in range(1, 21):
    print(number)

print("\nOne million list:")
print(f"First number: {million[0]}")
print(f"Last number: {million[-1]}")
print(f"min: {min(million)}")
print(f"max: {max(million)}")
print(f"sum: {sum(million)}")

print("\nOdd numbers from 1 to 20:")
for number in odd_numbers:
    print(number)

print("\nMultiples of 3 from 3 to 30:")
for number in threes:
    print(number)

print("\nFirst 10 cubes:")
for cube in cubes:
    print(cube)

print("\nFirst 10 cubes (list comprehension):")
print(cubes_comprehension)
