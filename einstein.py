#Ask the user for mass
mass = int(input("Mass in kg: "))

#Calculate energy using Einstein's formula
energy = mass * 300000000 ** 2

#Show the result cleaned up
print(f"Energy stored: {energy:,} joules")