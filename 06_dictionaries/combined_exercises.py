data = {
    'person': {
        'first_name': 'Ada',
        'last_name': 'Lovelace',
        'age': 36,
        'city': 'London',
    },
    'favorite_numbers': {
        'alice': 7,
        'bob': 42,
        'charlie': 13,
        'diana': 21,
        'eve': 3,
    },
    'glossary': {
        'variable': 'A named location in memory used to store a value.',
        'list': 'An ordered, mutable collection of items.',
        'dictionary': 'A collection of key-value pairs.',
        'loop': 'A construct that repeats a block of code.',
        'function': 'A reusable block of code that performs a specific task.',
    },
}

# --- چاپ شخص ---
print("=" * 40)
print("PERSON")
print("=" * 40)
for key, value in data['person'].items():
    print(f"{key}: {value}")

# --- چاپ اعداد مورد علاقه ---
print("\n" + "=" * 40)
print("FAVORITE NUMBERS")
print("=" * 40)
for name, number in data['favorite_numbers'].items():
    print(f"{name.title()}'s favorite number is {number}.")

# --- چاپ واژه‌نامه ---
print("\n" + "=" * 40)
print("GLOSSARY")
print("=" * 40)
for word, meaning in data['glossary'].items():
    print(f"{word.title()}:\n    {meaning}\n")
