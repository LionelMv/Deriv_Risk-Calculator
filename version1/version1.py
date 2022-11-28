print("**Risk Calculator for Volatility 50 (1s)**")
lowest_lot = 0.005

account_balance = float(input("Enter account balance: "))
entry_price = float(input("Entry price: "))
stop_price = float(input("Stop loss price: "))
risk_percent = float(input("Enter risk in percentage: "))
print()
num_of_pips = entry_price - stop_price
lowest_lot_amt = num_of_pips / 1000 #The 1000 is dependent on pair
risk_amount = account_balance * risk_percent / 100
lot_to_use = risk_amount / lowest_lot_amt * 0.001 #The 0.001 is dependent on pair

#specific to pair for now.
if lot_to_use <= 0.005:
    print("The minimum lot you can use is 0.005")
    print("Total risk = {:.2f}".format(lowest_lot_amt * 5))
else:
    print("The lot to use is: {:.4f}".format(lot_to_use))
    print("Total risk = {:.2f}".format(num_of_pips * lot_to_use))