Balance = 2000  # Opening Balance

while True:
    print("Welcome Buddy!")
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    Select = int(input("Enter the number: "))

    if Select == 1:
        Amount = int(input("Enter the withdraw amount: "))
        if Amount > Balance:
            print("Insufficient Balance")
        else:
            Balance -= Amount
            print(f"Rs. {Amount} withdraw. Balance is Rs. {Balance}")
    elif Select == 2:
        print(f"Your balance is Rs. {Balance}")
    elif Select == 3:
        print("Thanks Having nice day")
        break
    else:
        print("Invalid selection.")