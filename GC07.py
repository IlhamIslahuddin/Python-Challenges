def bank_withdrawal(balance):
    print (f"Current account balance: ${balance}")
    withdraw = float(input("How much does Pooja want to withdraw? "))
    if ((withdraw + 0.5) > balance) or (withdraw % 5 != 0):
        print ("Transaction failed.")
    else:
        total = withdraw + 0.5
        print (f"Successfully withdrew ${withdraw} + charged $0.5")
        balance_after = balance - total
        print (f"New account balance: ${balance_after}")

if __name__ == "__main__":
    bank_withdrawal(500.5)
