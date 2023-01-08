#!/usr/bin/python3

from get_details import obj1

def get_lot(lowest_lot, lowest_allowable_lot):
    lowest_stop_amt = obj1.num_of_pips * lowest_lot
    lot_to_use = obj1.risk_allowed_amount * lowest_lot / lowest_stop_amt

    if lot_to_use <= lowest_allowable_lot:
        return lowest_allowable_lot
    return lot_to_use

#There has to be another way to implement this
def total_risk(lowest_lot, lowest_allowable_lot):
    lowest_stop_amt = obj1.num_of_pips * lowest_lot
    lot_to_use = obj1.risk_allowed_amount * lowest_lot / lowest_stop_amt

    if lot_to_use <= lowest_allowable_lot:
        return obj1.num_of_pips * lowest_allowable_lot
    return obj1.num_of_pips * lot_to_use

