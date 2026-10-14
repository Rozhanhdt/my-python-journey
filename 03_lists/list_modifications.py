students = ['mona', 'mobina', 'parsa', 'tara', 'asma', 'dara', 'sasha', 'neda']

# Learn order of members
message_1 = f"{students[1].title()} is first in the class"
message_2 = f"{students[-1].title()} is second in the class"
message_3 = f"{students[0].title()} is third in the class"

print(message_1)
print(message_2)
print(message_3)

# Correcting a spelling error in the name
students[3] = 'taha'
students[7] = 'tina'

# Adding new member
students.insert(8, 'dina')
students.append('hana')

# Removing a member
del students[5]

swim_class = f'Students who are interested in swimming class: {students}'
print(swim_class)

popped_student = students.pop()
piano_class = f'Students who are interested in piano class: {students}'
yoga_class = f'Student who is interested in yoga class: {popped_student.title()}'

print(piano_class)
print(yoga_class)
