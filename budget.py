class Budget:
    def __init__(self, category, amount=0):
        self.category = category
        self.amount = amount

    def deposit(self, dep_amount):
        # print("Processing.....")
        self.amount += dep_amount
        print(f"{dep_amount}$ has been successfully deposited into {self.category}")
        return self.amount

    def withdrawal(self, withdraw_amount):
        # print("Processing.....")
        if withdraw_amount > self.amount:
            print("The withdrawal amount is more than the budget balance")
        else:
            self.amount -= withdraw_amount
            print(f"You have withdrawn {withdraw_amount}$ from {self.category}")
            return self.amount

    def budget_bal(self):
        # print("Processing.....")
        print(f"Your current balance in {self.category} is {self.amount}$")

    def transfer_amount(self, cat2, amt):
        self.withdrawal(amt)
        cat2.deposit(amt)


food = Budget("Food", 300)
games = Budget("Games")
food.withdrawal(100)
games.deposit(50)
food.transfer_amount(games, 50)
games.budget_bal()
food.budget_bal()
