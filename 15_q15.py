# calculate profit and loss percentage

cost_price = 500
selling_price = 600

# check profit
if selling_price > cost_price:

    # calculate profit
    profit = selling_price - cost_price

    # calculate profit percentage
    profit_percentage = (profit / cost_price) * 100

    print("Profit =", profit)
    print("Profit Percentage =", profit_percentage, "%")

# check loss
elif cost_price > selling_price:

    # calculate loss
    loss = cost_price - selling_price

    # calculate loss percentage
    loss_percentage = (loss / cost_price) * 100

    print("Loss =", loss)
    print("Loss Percentage =", loss_percentage, "%")

# no profit no loss
else:
    print("No Profit No Loss")