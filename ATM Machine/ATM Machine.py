import random  

class Account: 
    depositFrequency = 4 
    transactionMax = 40000 

    # Constructor for the Account object
    def __init__(self, id, balance=0, withdrawalDailyMax=50000, 
                 withdrawalFrequency=3, withdrawalTransactionMax=20000, 
                 depoDailyMax=150000, depositFrequency=4, depoTransactionMax=40000): 
        
        self.id = id 
        self.balance = balance 
        # Withdrawal attributes
        self.withdrawalDailyMax = withdrawalDailyMax 
        self.withdrawalFrequency = withdrawalFrequency 
        self.withdrawalTransactionMax = withdrawalTransactionMax 
        # Deposit attributes
        self.depoDailyMax = depoDailyMax 
        self.depositFrequency = depositFrequency 
        self.depoTransactionMax = depoTransactionMax 
    
    # Getter methods 
    def getId(self): 
        return self.id 
    
    def getBalance(self): 
        return self.balance 
    
    def getWithdrawalFrequency(self): 
        return self.withdrawalFrequency 
    
    def getWithdrawalTransactionMax(self): 
        return self.withdrawalTransactionMax 
    
    def getWithdrawalDailyMax(self): 
        return self.withdrawalDailyMax 
    
    def getDepoDailyMax(self): 
        return self.depoDailyMax 
    
    def getDepositFrequency(self): 
        return self.depositFrequency 
    
    def getDepoTransactionMax(self): 
        return self.depoTransactionMax 

    # Withdraw function
    def withdraw(self, amount): 
        if amount > self.withdrawalTransactionMax:
            print(f"Transaction limit exceeded! Maximum per transaction is {self.withdrawalTransactionMax}")
            return False
        elif amount > self.balance:
            print("Insufficient funds.")
            return False
        else:
            self.balance -= amount 
            self.withdrawalFrequency -= 1
            return True

    # Deposit function
    def deposit(self, amount): 
        if amount > self.depoTransactionMax:
            print(f"Transaction limit exceeded! Maximum per transaction is {self.depoTransactionMax}")
            return False
        else:
            self.balance += amount  
            self.depositFrequency -= 1
            return True

# Function to create accounts
def create_accounts():
    accounts = []
    for i in range(1000, 9999):  # Using a smaller range for testing
        accounts.append(Account(i, random.randint(0, 50000)))  # Random balance
    return accounts

# Function to find an account by ID
def find_account(accounts, id):
    for acc in accounts:
        if acc.getId() == id:
            return acc
    return None

# ATM process
def atm_process(accounts):
    while True:
        try:
            id = int(input("\nPlease Enter Your account PIN: "))
            if 1000 <= id <= 9999:
                break
            print("Invalid PIN. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    account = find_account(accounts, id)

    if not account:
        print("Account not found!")
        return

    while True:
        print("\n1 - Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Quit ")
        try:
            selection = int(input("Enter your selection: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if selection == 1:
            print(f"Your Balance is: {account.getBalance()}")

        elif selection == 2:
            print(f"Your Balance is: {account.getBalance()}")
            if account.getWithdrawalFrequency() == 3:
                print("You have reached your withdrawal limit for today.")
                continue
            
            try:
                amt = float(input("\nEnter amount to withdraw: "))
                if account.withdraw(amt):
                    print(f"Updated Balance: {account.getBalance()}")
                    print(f"You have {account.getWithdrawalFrequency()} withdrawal(s) remaining.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif selection == 3:
            print(f"Your Balance is: {account.getBalance()}")
            if account.getDepositFrequency() == 0:
                print("You have reached your deposit limit for today.")
                continue
            
            try:
                amt = float(input("\nEnter amount to deposit: "))
                if account.deposit(amt):
                    print(f"Updated Balance: {account.getBalance()}")
                    print(f"You have {account.getDepositFrequency()} deposit(s) remaining.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif selection == 4:
            check = input("Are you sure you want to quit? (Yes/No): ").strip().lower()
            if check == "yes":
                print("\nYour Transaction is complete.")
                print(f"Transaction number: {random.randint(10000, 1000000)}")
                print("Thanks for choosing us as your bank!")
                break
        else:
            print("\nInvalid selection, please try again.")

# Main function
def main():
    accounts = create_accounts()
    atm_process(accounts)

# Run the program
if __name__ == "__main__":
    main()
