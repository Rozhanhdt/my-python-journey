# Create a list of authors
authors = ['Dostoevsky', 'Camus', 'Tolstoy', 'Beckett', 'Kafka']

# 1. Print the list
print("Original list:")
print(authors)

# 2. Access elements by index
print(f"\nFirst author: {authors[0]}")
print(f"Last author: {authors[-1]}")

# 3. Use individual values in f-strings
print(f"\nMy favorite book is by {authors[0]}.")

# 4. Modify an element
authors[1] = 'Sartre'
print("\nAfter modifying index 1:")
print(authors)

# 5. Append an element
authors.append('Hesse')
print("\nAfter append:")
print(authors)

# 6. Insert an element at a specific position
authors.insert(0, 'Dostoevsky')
print("\nAfter insert at index 0:")
print(authors)

# 7. Remove an element by index with del
del authors[0]
print("\nAfter removing index 0 with del:")
print(authors)

# 8. Use pop() to remove and store last item
popped = authors.pop()
print(f"\nPopped author: {popped}")
print("List after pop:")
print(authors)

# 9. Use remove() to remove by value
authors.remove('Kafka')
print("\nAfter remove('Kafka'):")
print(authors)

# 10. Use sorted() (temporary sort)
print("\nSorted temporarily:")
print(sorted(authors))
print("Original order preserved:")
print(authors)

# 11. Use sorted() with reverse=True
print("\nSorted reverse temporarily:")
print(sorted(authors, reverse=True))

# 12. Use reverse()
authors.reverse()
print("\nAfter reverse():")
print(authors)

# 13. Use sort() (permanent alphabetical)
authors.sort()
print("\nAfter sort():")
print(authors)

# 14. Use sort(reverse=True)
authors.sort(reverse=True)
print("\nAfter sort(reverse=True):")
print(authors)

# 15. Use len()
print(f"\nNumber of authors in list: {len(authors)}")
