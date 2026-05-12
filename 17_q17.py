# Define input variables
principal = 10000
rate = 5
time = 2

# Step 1: Calculate the multiplier (1 + R/100)
multiplier = 1 + (rate / 100)  # Ye 1.05 ho jayega

# Step 2: Use ** for power (multiplier ki power time)
total_amount = principal * (multiplier ** time)

# Step 3: Interest = Total Amount - Original Principal
compound_interest = total_amount - principal

# Display the final output
print("Compound Interest =", compound_interest)