# Store locations in a list (not in alphabetical order)
places = ['Milan', 'Tokyo', 'New York', 'London', 'Vancouver']

# Print original list
print("Original list:")
print(places)

# Print in alphabetical order without modifying the list
print("\nSorted alphabetically (temporary):")
print(sorted(places))

# Show list is still in original order
print("\nOriginal list is still intact:")
print(places)

# Print in reverse-alphabetical order without modifying the list
print("\nSorted in reverse-alphabetical order (temporary):")
print(sorted(places, reverse=True))

# Show list is still in original order
print("\nOriginal list is still intact:")
print(places)

# Use reverse() to change the order
print("\nReversed with reverse():")
places.reverse()
print(places)

# Use reverse() again to restore original order
print("\nReversed back to original:")
places.reverse()
print(places)

# Use sort() to change to alphabetical order permanently
print("\nSorted alphabetically (permanent):")
places.sort()
print(places)

# Use sort() to change to reverse-alphabetical order permanently
print("\nSorted reverse-alphabetically (permanent):")
places.sort(reverse=True)
print(places)
