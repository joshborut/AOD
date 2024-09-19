import csv


# Returns the number of penguins of a certain species given which island to search (or all islands)
def get_species_count(species, island="all"):
    # Open dataset
    with open('datasets/penguins_size.csv', 'r') as f:
        # Parse data to dict
        data = csv.DictReader(f)
        # Initialize count
        count = 0
        # Loop through individual penguins
        for penguin in data:
            # Check if we are looking across all islands
            if island == "all":
                # Check for species match
                if penguin['species'] == species:
                    # Increment counter
                    count += 1
            else:
                # Check for species and island match
                if penguin['species'] == species and penguin['island'] == island:
                    # increment counter
                    count += 1
        # Return count
        return count


# Returns a dictionary with the averages for a specified category
def get_penguin_avgs(category):
    # Open dataset
    with open('datasets/penguins_size.csv', 'r') as f:
        # Parse data to dict
        data = csv.DictReader(f)
        # Initialize dict
        sorted_data = {}
        # Loop through individual penguins
        for penguin in data:
            # Check if the data in the category is NA
            if penguin[category] != 'NA':
                # Add to dict if species is not in it
                if penguin['species'] not in sorted_data:
                    sorted_data[penguin['species']] = []
                    sorted_data[penguin['species']].append(float(penguin[category]))
                # Add value to species specific key
                else:
                    sorted_data[penguin['species']].append(float(penguin[category]))
        # Loop through each species in dict
        for species in sorted_data.keys():
            # Average the list of values for each species
            sorted_data[species] = (sum(sorted_data[species]) / len(sorted_data[species]))
        # Return sorted data
        return sorted_data


data_max = lambda data: max(data, key=data.get)

# 1: Beak size
beak_averages = get_penguin_avgs('culmen_length_mm')
print(f"Average beak lengths: {beak_averages}")
max_beak_species = data_max(beak_averages)
print(f"{max_beak_species} has the highest beak length, which is {beak_averages[max_beak_species]}\n")

# 2: Mass
mass_averages = get_penguin_avgs('body_mass_g')
print(f"Average masses: {mass_averages}")
max_mass_species = data_max(mass_averages)
print(f"{max_mass_species} has the highest mass, which is {mass_averages[max_mass_species]}\n")

# 3: Number of Chinstrap penguins on Dream Island
print(f"Number of Chinstrap penguins are on Dream Island: {get_species_count('Chinstrap', 'Dream')}")