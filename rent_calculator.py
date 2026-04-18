while True:
    print("\n--- Room Expense Calculator ---")

    rent = int(input("Rent: "))
    food = int(input("Food: "))
    units = float(input("Electricity Units: "))
    rate = int(input("Rate Per Unit: "))
    other = int(input("Other Expenses: "))
    members = int(input("Members: "))

    electricity_bill = units * rate
    total = rent + food + electricity_bill + other
    per_person = total / members

    print("\nTotal Expense:", total)
    print("Per Person:", round(per_person, 2))

    choice = input("\nDo you want to exit? (yes/no): ").lower()

    if choice == "yes":
        print("Thank You!")
        break