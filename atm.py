
class Atm:
    def __init__(self, pin, cardNum):
        self.pin = pin
        self.cardNum = cardNum

    def cashWithdrawl(self, amount):
        newAmount = 5000 - amount
        print("CashWithdrawl succesful, You have widrawn"+str(amount)+". Remaining balance is"+str(newAmount))

    def balanceEquiry(self):
        print("You have as much as you want in your bank account")


def main():
    cardNumber=input("Insert your card number")
    pinNumber=input("Enter your pin number")

    newUser = Atm(pinNumber, cardNumber)
    print("Choose your activity:")
    print("1.Balance Enquiry 2.Cash Withdrawl")
    activity = int(input("Enter activity number:"))
    if (activity == 1):
        newUser.balanceEquiry()
    elif(activity == 2):
        amount = int(input("Enter the amount"))
        newUser.cashWithdrawl(amount)
    else:
        print("Enter a valid number")
if __name__ == "__main__":
    main()

