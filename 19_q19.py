# Calculate percentage increase or decrease

initial_value = 200
final_value = 250

# formula
percentage_change = ((final_value - initial_value) / initial_value) * 100

# check increase or decrease
if final_value > initial_value:
    print("Percentage Increase =", percentage_change, "%")
else:
    print("Percentage Decrease =", percentage_change, "%")