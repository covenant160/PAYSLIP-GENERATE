mmlcode = "*151#"
enter = input("Enter MML code: ")

if enter == mmlcode:
    print("Please select your currency:")
    print("1. Zimbabwe gold")
    print("2. United States Dollar")
    zwc = input("Enter your choice (1/2): ")

    if zwc == "1" or zwc == "2":
        pincode = input("Please enter your pincode: ")

        if pincode == "1984":
            print("1. EcoCash menu")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check balance")
            print("5. Send money")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "5":
                recipient_phone_number = input("Enter recipient's phone number: ")
                amount = float(input("Enter amount to send: "))
                print(f"Sending ${amount} to {recipient_phone_number}...")
                print("Transaction successful!")
            elif choice == "6":
                print("Exiting...")
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Incorrect pincode.")
    else:
        print("Invalid selection.")
else:
    print("Invalid MML code.")

