from re import match


withdraw = 0
deposit = 0

def main():
    global balance
    count = 0
    
    dashboard()

    while count < 1: 
        cmd = input("Command usage: 'balance' or deposit <num>'\n")

        match cmd:
            case "balance":
                balance()
                print("Your balance is: ", balance)

            case "deposit (\d+)":
                amount = int(match.group(1))
                deposit(cmd)
                print("Your new balance is: ", balance)

            case "withdraw ":
                withdraw(cmd)
                print("Your new balance is: ", balance)

            case "exit":
                count = 1

            case _:
                print("Select a valid option. \n")

    return cmd

def dashboard():
    print("Welcome to Bank App\n")
    print("1) Check Balance\n")
    print("2) Deposit\n")
    print("3) Withdraw\n")

def balance():
    return balance

def deposit(cmd):

    if cmd >= 0:
        balance = balance + cmd

    return balance

def withdraw(cmd):
    if cmd >= 0 and cmd <= balance:
        balance = balance - cmd

    return balance

main()