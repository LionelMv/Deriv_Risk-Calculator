"""
To avoid repetition I am using this file to create functions
to be called by other files.
"""

if __name__ == "__main__":
    lowest_lot = 0.005

    account_balance = float(input("Enter account balance: "))
    entry_price = float(input("Entry price: "))
    stop_price = float(input("Stop loss price: "))
    risk_percent = float(input("Enter risk in percentage: "))