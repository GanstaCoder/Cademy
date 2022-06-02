# Loops Examples:


board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
    print(game)

for sport_game in sport_games:
    print(sport_game)

# Loop in range

promise = "I will finish the python loops module!"

for i in range(5):
    print(promise)

# Loop example 2

# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
    # Loop Body
    # Print if the condition is still true
    print("Loop Iteration - count <= 3 is still true")
    # Print the current value of count
    print("Count is currently " + str(count))
    # Increment count
    count += 1
    print(" ----- ")
print("While Loop ended")

# Your code below:
countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("We have liftoff!")

# Example 3

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# Your code below:
length = len(python_topics)
index = 0

while index < length:
    print("I am learning about " + python_topics[index])
    index += 1

# Avoid infinite loop

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    # students_period_A.append(student)
    print(student)

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
    if age < 21:
        continue
    print(age)

# Nest loop
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element

print(scoops_sold)

# Comparison

grades = [90, 88, 62, 76, 74, 89, 48, 57]

# One liner
scaled_grades = [num + 10 for num in grades]
print(scaled_grades)

# You can append
scaled_grades = []
for number in grades:
    scaled_grades.append(number + 10)

print(scaled_grades)


# Another example
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

# +++++++++++++++++++++++++++
single_digits = range(10)
squares = []

for item in single_digits:
    print(item)
    squares.append(item ** 2)

print(squares)

cubes = [item ** 3 for item in single_digits]
print(cubes)