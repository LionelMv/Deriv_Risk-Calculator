#!/usr/bin/python3

class Instrument:
    def __init__(self, acc_balance, ent_price, stp_price, risk_pct):
        self.acc_balance = acc_balance
        self.ent_price = ent_price
        self.stp_price = stp_price
        self.risk_pct = risk_pct
        self.num_of_pips = ent_price - stp_price
        self.risk_allowed_amount = acc_balance * (risk_pct / 100)

#Get details
account_balance = float(input("Enter account balance: "))
entry_price = float(input("Entry price: "))
stop_price = float(input("Stop loss price: "))
risk_percent = float(input("Enter risk in percentage: "))

obj1 = Instrument(account_balance, entry_price, stop_price, risk_percent)
