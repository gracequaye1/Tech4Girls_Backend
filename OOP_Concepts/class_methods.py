class BankAccount:
    # Class variable
    bank_name = "Tech4Girls Bank"

    def __init__(self, account_holder):
        """Initialize account holder and balance."""
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct money from the account, ensuring balance is not negative."""
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    @staticmethod
    def bank_policy():
        """Print a generic policy message."""
        print("Welcome to Tech4Girls Bank. Maintain a minimum balance of $10.")

    @classmethod
    def get_bank_name(cls):
        """Return the name of the bank."""
        return cls.bank_name


# Demonstration
# Create instances of BankAccount
account1 = BankAccount("Grace Okailey Quaye")
account2 = BankAccount("John Doe")

# Use instance methods
account1.deposit(100)
account1.withdraw(50)
account1.withdraw(60)  # Attempt to withdraw more than balance

# Use class method
print(f"Bank Name: {BankAccount.get_bank_name()}")

# Use static method
BankAccount.bank_policy()

# Another example for the second account
account2.deposit(200)
account2.withdraw(80)
