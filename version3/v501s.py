#!/usr/bin/python3

print("**Risk Calculator for Volatility 50 (1s)**")

from instruments import obj1

lowest_allowable_lot = 0.005
lowest_lot = 0.001
lowest_lot_amt = obj1.num_of_pips / 1000 #1000 because of the 0.005
lot_to_use = obj1.risk_allowed_amount / lowest_lot_amt * 0.001 #The 0.001 is because of the 0.005

if lot_to_use <= lowest_lot:
    print("The minimum lot you can use is: " + lowest_lot)
    print("Total risk = {:.2f}".format(lowest_lot_amt * 5))
else:
    print("The lot to use is: {:.4f}".format(lot_to_use))
    print("Total risk = {:.2f}".format(obj1.num_of_pips * lot_to_use))
