entry_price = float(input("Enter entry price: "))
stop_price = float(input("Enter stop price: "))
account_balance = float(input("Enter account size: "))

num_of_pips = entry_price - stop_price

print("Num of pips = ", num_of_pips)

risk_percent = account_balance * 1 /100
