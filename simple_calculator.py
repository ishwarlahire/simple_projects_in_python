while True:
    num1 = int(input("Enter First Number"))
    num2 = int(input("Enter Second Number"))
    task = int(input("Please select one option \n for Addition press 1 \n for Subtraction press 2 \n for multiplication press 3 \n for division press 4 \n for exit form calculator enter 5\n"))
    if task == 1:
        print((num1 + num2))
    elif task == 2:
        print((num1 - num2))
    elif task == 3:
        print((num1 * num2))
    elif task == 4:
        print((num1 / num2))  
    elif task == 5:
        print("thank you for used my calcutor")
        break
    else :
        print("Enter correct option")