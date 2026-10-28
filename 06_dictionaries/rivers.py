rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

# A sentence about each river
print("--- River sentences ---")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# River names only
print("\n--- River names ---")
for river in rivers.keys():
    print(river.title())

# Country names only
print("\n--- Country names ---")
for country in rivers.values():
    print(country.title())
