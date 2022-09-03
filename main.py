class Machine:
    def __init__(self):
        self.balance = 0
        self.red = 0
        self.yellow = 0
        self.pennies = 0
        self.half_dollar = 0
        self.dollar_coin = 0


    def insert_nickel(self):
        self.balance = self.balance + 5
        print('New balance: ' + str(self.balance))
    

    def insert_dime(self):
        self.balance = self.balance + 10
        print('New balance: ' + str(self.balance))


    def insert_quarter(self):
        self.balance = self.balance + 25
        print('New balance: ' + str(self.balance))
    

    def insert_penny(self):
        self.pennies = self.pennies + 1


    def insert_half_dollar(self):
        self.half_dollar = self.half_dollar + 1


    def insert_dollar_coin(self):
        self.dollar_coin = self.dollar_coin + 1


    def red_lever(self):
        if (self.pennies > 0) or (self.half_dollar > 0) or (self.dollar_coin > 0):
            print("Returned " + str(self.pennies) + " pennies, " + str(self.half_dollar) + " half dollars, and " + str(self.dollar_coin) + " dollar coins.")
            self.pennies = 0
            self.half_dollar = 0
            self.dollar_coin = 0
        if self.balance < 5:
            print('Not enough balance')
        else:
            self.balance = self.balance - 5
            self.red = self.red + 1
            print('New balance: ' + str(self.balance))
            print("Number of red gumballs: " + str(self.red))
            print("Number of yellow gumballs: " + str(self.yellow))


    def yellow_lever(self):
        if (self.pennies > 0) or (self.half_dollar > 0) or (self.dollar_coin > 0):
            print("Returned " + str(self.pennies) + " pennies, " + str(self.half_dollar) + " half dollars, and " + str(self.dollar_coin) + " dollar coins.")
            self.pennies = 0
            self.half_dollar = 0
            self.dollar_coin = 0
        if self.balance < 10:
            print('Not enough balance')
        else:
            self.balance = self.balance - 10
            self.yellow = self.yellow + 1
            print('New balance: ' + str(self.balance))
            print("Number of red gumballs: " + str(self.red))
            print("Number of yellow gumballs: " + str(self.yellow))

    
    def return_my_change(self):
        print("Returned " + str(self.balance) + " cents")
        self.balance = 0


def main():
    machine = Machine()
    print("Valid actions:")
    print("PENNY - insert penny")
    print("NICKEL - insert nickel")
    print("DIME - insert dime")
    print("QUARTER - insert quarter")
    print("HALF DOLLAR - insert half dollar")
    print("DOLLAR COIN - insert dollar coin")
    print("RED - pull red lever")
    print("YELLOW - pull yellow lever")
    print("CHANGE - return change")
    print("DONE - finish using machine")
    x = 1
    while(x==1):
        action = input("\nEnter action: ")
        action = action.lower()
        if action == "penny":
            machine.insert_penny()
        elif action == "nickel":
            machine.insert_nickel()
        elif action == "dime":
            machine.insert_dime()
        elif action == "quarter":
            machine.insert_quarter()
        elif action == "half dollar":
            machine.insert_half_dollar()
        elif action == "dollar coin":
            machine.insert_dollar_coin()
        elif action == "red":
            machine.red_lever()
        elif action == "yellow":
            machine.yellow_lever()
        elif action == "change":
            machine.return_my_change()
        elif action == "done":
            x = 0
        else:
            print("Invalid action")


if __name__ == "__main__":
    main()
