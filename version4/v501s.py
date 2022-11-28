#!/usr/bin/python3

print("**Risk Calculator for Volatility 50 (1s)**")

from instruments import obj1

lowest_allowable_lot = 0.005
lowest_lot = 0.001

#This section should be made modular in next version.
lowest_stop_amt = obj1.num_of_pips * lowest_lot
lot_to_use = obj1.risk_allowed_amount * lowest_lot / lowest_stop_amt

if lot_to_use <= lowest_allowable_lot:
    print("The minimum lot you can use is: ", lowest_allowable_lot)
    print("Total risk = {:.2f}".format(obj1.num_of_pips * lowest_allowable_lot))
else:
    print("The lot to use is: {:.3f}".format(lot_to_use))
    print("Total risk = {:.2f}".format(obj1.num_of_pips * lot_to_use))