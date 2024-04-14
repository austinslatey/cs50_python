# Prompt user for mass in kilograms
mass = int(input("Enter the mass in kilograms: "))

# Calculate the energy in Joules using Einstein's equation
speed_of_light = 300000000
energy = mass * speed_of_light ** 2

# Display the equivalent energy in Joules
print("The equivalent energy is:", energy, "Joules")