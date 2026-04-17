def main():
    num1 = int(input("Enter First Number"))
    num2 = int(input("Enter Second Number"))
    task = int(input("Please select one option \n for Addition press 1 \n for Subtraction press 2 \n for multiplication press 3 \n for division press 4 \n"))
    return num1, num2, task

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

num1, num2, task = main()

if task == 1:
    print(add(num1,num2))
elif task == 2:
    print(sub(num1,num2))
elif task == 3:
    print(mul(num1,num2))
elif task == 4:
    print(div(num1,num2))
else :
    print("Enter correct option")
    