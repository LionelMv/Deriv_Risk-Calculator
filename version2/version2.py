print("**Risk Calculator for Volatility 50 (1s)**")
lowest_allowable_lot = 0.005
lowest_lot = 0.001

account_balance = float(input("Enter account balance: "))
entry_price = float(input("Entry price: "))
stop_price = float(input("Stop loss price: "))
risk_percent = float(input("Enter risk in percentage: "))
print()
num_of_pips = entry_price - stop_price
lowest_stop_amt = num_of_pips * lowest_lot
risk_allowable_amount = account_balance * risk_percent / 100
lot_to_use = risk_allowable_amount * lowest_lot / lowest_stop_amt
#specific to pair for now.
if lot_to_use <= lowest_allowable_lot:
    print("The minimum lot you can use is: ", lowest_allowable_lot)
    print("Total risk = {:.2f}".format(num_of_pips * lowest_allowable_lot))
else:
    print("The lot to use is: {:.4f}".format(lot_to_use))
    print("Total risk = {:.2f}".format(num_of_pips * lot_to_use))
