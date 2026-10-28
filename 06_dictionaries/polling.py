favorite_languages = {
    'roshana': 'python',
    'liana': 'c',
    'niloofar': 'ruby',
    'elnaz': 'python',
}

# لیست افرادی که باید در نظرسنجی شرکت کنند
people = [
    'roshana', 'liana', 'niloofar', 'elnaz',
    'mona', 'mohadeseh', 'yeganeh',
]

for name in people:
    if name in favorite_languages:
        print(f"Thank you, {name.title()}, for responding!")
    else:
        print(f"{name.title()}, please take our favorite languages poll!")
