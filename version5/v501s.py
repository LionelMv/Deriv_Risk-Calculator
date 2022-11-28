#!/usr/bin/python3

print("**Risk Calculator for Volatility 50 (1s)**")

from get_lot_risk import get_lot, total_risk

lowest_allowable_lot = 0.005
lowest_lot = 0.001

print("Lot size is: {:.3f}".format(get_lot(lowest_allowable_lot, lowest_lot)))
print("Total risk is {:.2f}".format(total_risk(lowest_allowable_lot, lowest_lot)))