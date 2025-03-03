# Get group sizes
n = int(input("Enter number of domestic animals (N): "))
x = int(input("Enter number of wild animals (X): "))

# Initialize lists
all_animals = []

# Collect domestic animals
print("\nEnter domestic animals:")
for i in range(n):
    animal = input(f"Animal {i+1}: ")
    all_animals.append(animal)
    print("Current animals:", all_animals)

# Collect wild animals
print("\nEnter wild animals:")
for i in range(x):
    animal = input(f"Animal {i+1}: ")
    all_animals.append(animal)
    print("Current animals:", all_animals)

# Final output
print("\nAll animals:", all_animals)