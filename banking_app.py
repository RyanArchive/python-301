class Bank:
    balance = 0.00

    def cast(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        return amount

    def deposit(self, amount):
        self.balance = self.balance + self.cast(amount)
        self.save_log("Deposit", amount, "Success")

    def withdraw(self, amount):
        amount = self.cast(amount)
        status = "Success"
        if amount < self.balance:
            self.balance = self.balance - amount
        else:
            status = "Failed"
            print("Entered amount is more than the balance")
        self.save_log("Withdrawal", amount, status)

    def save_log(self, action, amount, status):
        with open("transac_log.txt", "a") as file:
            file.write(f"Action: {action}")
            file.write(f"\nAmount: {amount}")
            file.write(f"\nStatus: {status}")
            file.write(f"\nNew Balance: {self.balance}\n\n")

bank = Bank()

print("[D] Deposit")
print("[W] Withdraw")
print("[X] Exit")

while True:
    action = ""

    while action not in ["D", "W", "X"]:
        action = input("\nSelect action [W/D/X]: ")
        action = action.upper()

    if action == "D":
        amount = input("Enter amount (deposit): ")
        bank.deposit(amount)

    elif action == "W":
        amount = input("Enter amount (withdraw): ")
        bank.withdraw(amount)

    elif action == "X":
        exit()

    print(f"New Balance: P {bank.balance}")