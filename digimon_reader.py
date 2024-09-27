import csv


# 1. Finds average HP of all Digimon
def get_average_hp():
    # Open the dataset
    with open('datasets/digimon.csv', 'r') as f:
        # Parse the dataset to an iterable
        data = csv.DictReader(f)
        # Initialize the HP list
        hp_list = []
        # Loop through each row/digimon
        for digimon in data:
            # Add the HP of the Digimon to the HP list
            hp_list.append(float(digimon['HP']))
        # Average the values from the HP list
        average_hp = (sum(hp_list) / len(hp_list))
        # Return the average value
        return average_hp


print(get_average_hp())


# 2. Counts the number of Digimon with specific value in a category
def count_digimon(category, value):
    # Open the dataset
    with open('datasets/digimon.csv', 'r') as f:
        # Parse the dataset to an iterable
        data = csv.DictReader(f)
        # Initialize the counter
        count = 0
        # Loop through each row/Digimon
        for digimon in data:
            # Check if the desired condition is true
            if digimon[category] == value:
                # Increment the counter
                count += 1
                # Return the total count
        return count


print(count_digimon("Type", "Vaccine"))


# 3. Finds team of up to 3 with memory of 15 or less and at least an attack of 300
def get_team():
    # Open the dataset
    with open('datasets/digimon.csv', 'r') as f:
        # Parse the dataset to an iterable
        data = csv.DictReader(f)
        # Loop through each row/Digimon
        for digimon_1 in data:
            # Store digimon_1 Memory
            digimon_1_mem = float(digimon_1['Memory'])
            # Store digimon_1 Atk
            digimon_1_atk = float(digimon_1['Atk'])
            # Check if digimon_1 fulfills the conditions
            if digimon_1_mem <= 15 and digimon_1_atk >= 300:
                # Return the team with just digimon_1
                return [digimon_1['Digimon']]
            # Move to next layer of iteration
            else:
                # Loop through each row/Digimon
                for digimon_2 in data:
                    # Store digimon_2 Memory
                    digimon_2_mem = float(digimon_2['Memory'])
                    # Store digimon_2 Atk
                    digimon_2_atk = float(digimon_2['Atk'])
                    # Check if the team with digimon_1 and digimon_2 fulfills the conditions
                    if (digimon_1_mem + digimon_2_mem) <= 15 and (digimon_1_atk + digimon_2_atk) >= 300:
                        # Return the team with digimon_1 and digimon_2
                        return [digimon_1['Digimon'], digimon_2['Digimon']]
                    # Move to next layer of iteration
                    else:
                        # Loop through each row/Digimon
                        for digimon_3 in data:
                            # Store digimon_3 Memory
                            digimon_3_mem = float(digimon_3['Memory'])
                            # Store digimon_3 Atk
                            digimon_3_atk = float(digimon_3['Atk'])
                            # Check if the team with digimon_1, digimon_2, and digimon_3 fulfills the conditions
                            if (digimon_1_mem + digimon_2_mem + digimon_3_mem) <= 15 \
                                    and (digimon_1_atk + digimon_2_atk + digimon_3_atk) >= 300:
                                # Return the team with digimon_1, digimon_2, and digimon_3
                                return [digimon_1['Digimon'], digimon_2['Digimon'], digimon_3['Digimon']]


print(get_team())
