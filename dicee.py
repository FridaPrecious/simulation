import pandas as pd 
import random

max_run=1000

# #initialisation of the faces 
# faces = ['1', '2', '3', '4', '5', '6']


# Counters for each face and face initialisation
face_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

def face_choice():
    return random.uniform(0 ,1)

#function for simulating dice
for _ in range(max_run):
    x = face_choice()
    
    if (0 <= x < 1/6):
        face_counts[1] += 1
    elif(1/6 <=x <2/6):
        face_counts[2] += 1
    elif(2/6 <=x <3/6):
        face_counts[3] += 1
    elif(3/6 <=x <4/6):
        face_counts[4] += 1
    elif(4/6 <=x <5/6):
        face_counts[5] += 1
    else:
        face_counts[6] += 1

# Calculate frequencies and percentages
total_rolls = sum(face_counts.values())
frequencies = {face: count for face, count in face_counts.items()}
percentages = {face: count / total_rolls * 100 for face, count in face_counts.items()}

# Create a DataFrame
df = pd.DataFrame({'Face': sorted(frequencies.keys()), 'Frequency': [frequencies[face] for face in sorted(frequencies.keys())], 'Percentage': ['{:.2f}%'.format(percentages[face]) for face in sorted(percentages.keys())]})

# Add a row for the sum of the frequencies
df.loc[len(df.index)] = ['Total', sum(df['Frequency']), '']


# Print the DataFrame
#print(df)
print(df.to_string(index=False))

