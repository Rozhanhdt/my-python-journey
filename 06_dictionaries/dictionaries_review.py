people = [
    {
        'first_name': 'sara',
        'last_name': 'nouri',
        'age': 29,
        'home': 'shiraz',
        'favorite_numbers': [7, 11],
        'favorite_places': ['isfahan', 'kyoto'],
    },
    {
        'first_name': 'reza',
        'last_name': 'karimi',
        'age': 34,
        'home': 'tabriz',
        'favorite_numbers': [3],
        'favorite_places': ['rome', 'lisbon'],
    },
]

places = {
    'isfahan': {
        'country': 'iran',
        'population': 2_000_000,
        'language': 'persian',
        'founded': 1598,
        'note': 'Naqsh-e Jahan Square is at the center of the old city.',
    },
    'kyoto': {
        'country': 'japan',
        'population': 1_460_000,
        'language': 'japanese',
        'founded': 794,
        'note': 'It was Japan\'s capital for more than a thousand years.',
    },
    'rome': {
        'country': 'italy',
        'population': 2_800_000,
        'language': 'italian',
        'founded': -753,
        'note': 'The Colosseum still stands near the city center.',
    },
}

print("=" * 40)
print("PEOPLE")
print("=" * 40)

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"\n{full_name}")
    print(f"  Age: {person['age']}")
    print(f"  Home: {person['home'].title()}")

    print("  Favorite numbers:")
    for number in person['favorite_numbers']:
        print(f"    {number}")

    print("  Favorite places:")
    for place in person['favorite_places']:
        if place in places:
            country = places[place]['country'].title()
            print(f"    - {place.title()} ({country})")
        else:
            print(f"    - {place.title()}")

print("\n" + "=" * 40)
print("PLACES")
print("=" * 40)

for name, info in places.items():
    country = info['country'].title()
    language = info['language'].title()
    population = f"{info['population']:,}"
    founded = info['founded']
    if founded < 0:
        founded_text = f"{abs(founded)} BCE"
    else:
        founded_text = str(founded)

    print(f"\n{name.title()}, {country}")
    print("-" * 32)
    print(f"Population: about {population}")
    print(f"Language:   {language}")
    print(f"Founded:    {founded_text}")
    print(f"Note:       {info['note']}")
