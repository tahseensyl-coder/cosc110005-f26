# MAIN INFORMATION
# Course: COSC 1100
# Assignment: Numeric and String Data
# Author: Michael Chisholm,Tahseenur Rahman
# Date: September 24, 2026

# PLAN

# 1. OUTPUT
# Display the number of ducks required.

# 2. INPUT
# Reservoir area = 5000 m2
# Duck length = 10 cm
# Duck width = 9 cm

# 3. PROCESS
# Convert cm to m
# Calculate duck area
# Calculate ducks required

# 4. PSEUDOCODE
# Get reservoir area
# Get duck dimensions
# Calculate duck area
# Calculate number of ducks
# Display result

# 5. DESK CHECK
# 9 cm / 100 = 0.09 m
# 10 cm / 100 = 0.10 m
# 0.09 x 0.10 = 0.009 m2
# 5000 / 0.009 = 555555.56



# PROGRAM

import math

reservoir_area = 5000

duck_length_cm = float(input("Enter the duck length in cm: "))
duck_width_cm = float(input("Enter the duck width in cm: "))

duck_length_m = duck_length_cm / 100
duck_width_m = duck_width_cm / 100

duck_area = duck_length_m * duck_width_m

ducks_required = math.ceil(reservoir_area / duck_area)

print(f"Reservoir area: {reservoir_area} m2")
print(f"Duck size: {duck_length_cm} cm x {duck_width_cm} cm")
print(f"Duck area: {duck_area} m2")
print(f"Ducks required: {ducks_required:,}")