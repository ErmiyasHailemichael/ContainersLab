# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

#################--START---#####################

students = ['Ermiyas', 'Anna', 'Ash', 'Cody', 'Colin', 'Cynthia', 'Ella']
print(students[1])
print(students[-1])

###############---END--#######################

# Exercise 2
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

#################--START---#####################

students = ['Ermiyas', 'Anna', 'Ash', 'Cody', 'Colin', 'Cynthia', 'Ella']
foods = ('pizza', 'pasta', 'salad', 'chicken', 'steak', 'burger','sandwich')

for food in foods:
    print(f'{food} is a good food')

for student in students:
    print(f'{student} is a good student')

###############---END--#######################

# Exercise 3
# Using a forloop, print just the last two food strings from foods.

#################--START---#####################

foods = ('pizza', 'pasta', 'salad', 'chicken', 'steak', 'burger','sandwich')

for food in foods[-2:]:
    print(food)

###############---END--#######################


# Exercise 4
# Create a dictionary named home_towncontaining the keys of city, stateand population.
# Print a string with this format:
# "I was born in city, state - population of population"

#################--START---#####################
home_town = { 
    'city': 'CMC',
    'state': 'Addis Ababa',
    'population': 4000000,
}

print(f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

###############---END--#######################

# Exercise 5
# Iterate over the key: value pairs in home_townand print a string for each item, for example:
# 	"city = Arcadia"
# 	"state = California"
# 	"population = 58000"

#################--START---#####################
home_town = {
    'city': 'Arcadia',
    'state': 'California',
    'population': 58000,
}

for key, value in home_town.items():
    print(f'{key} = {value}')
###############---END--#######################

# Exercise 6
# Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohortlist for each student name. Each dictionary should have this shape:
# {
# 	'student': 'Tina',
# 	'fav_food': 'Cheeseburger'
# }
# Iterate over cohortprinting out each element.

#################--START---#####################
cohorts = []

students = ['Ermiyas', 'Anna', 'Ash', 'Cody', 'Colin', 'Cynthia', 'Ella']
foods = ('pizza', 'pasta', 'salad', 'chicken', 'steak', 'burger','sandwich')

for i in range(len(students)):
    cohorts.append({'student': students[i], 'fav_food': foods[i]})

for student in cohorts:
    print(student)   

###############---END--#######################
# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_studentsa new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_studentsprinting out each string.

#################--START---#####################
students = ['Tina', 'Fred', 'Ash', 'Wilma', 'Colin', 'Cynthia', 'Ella']
awesome_students = [f'{student} is awesome!' for student in students]
print(awesome_students)

###############---END--#######################

# Exercise 8
# Using the tuple foodsand list comprehension within a for loop, print each food string that contains the letter a.

#################--START---#####################
foods = ('pizza', 'pasta', 'salad', 'chicken', 'steak', 'burger','sandwich')

for food in foods:
    if 'a' in food:
        print(food)
        
###############---END--#######################