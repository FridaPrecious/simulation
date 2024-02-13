import random
import prettytable

# Function to simulate rolling a dice
def roll_dice():
    return random.uniform(0, 1)

# Number of times to roll the dice
num_rolls = 1000

# Counters for each face
face_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Simulate rolling the dice and count the occurrences
for _ in range(num_rolls):
    result = roll_dice()
    for face in face_counts:
        if result <= face / 6:
            face_counts[face] += 1
            break

# Calculate frequencies and percentages
total_rolls = sum(face_counts.values())
frequencies = {face: count for face, count in face_counts.items()}
percentages = {face: count / total_rolls * 100 for face, count in face_counts.items()}

# Create a table
table = prettytable.PrettyTable(['Face', 'Frequency', 'Percentage'])
for face in sorted(frequencies.keys()):
    table.add_row([face, frequencies[face], '{:.2f}%'.format(percentages[face])])

# Print the table
print(table)
