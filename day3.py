# File_Handling,Exception, Decorators, Generators, Lambda, Map,  Filter
# 1. File Handling (5 Questions)
# Create a file data.txt and write your name in it.
file = open("data.txt","w+")
file.write("hello ishwar")
file.seek(0)
data = file.read()
print(data)
file.close()

# Read content from data.txt and print it.
file = open("data.txt","r")
data = file.read()
print(data)
file.close()

# Append "Python Developer" in same file.
file = open("data.txt","a+")
file.write(" Python Developer")
file.seek(0)
data = file.read()
print(data)


# Count total lines in a file.
file = open("data.txt","r")
data = file.readlines()
count = len(data)
print(count)

# Read a file and count how many times word "Python" appears.
file = open("data.txt","r")
data = file.read().split()
count = 0
for i in data:
    if i.lower() == "python":
        count+=1
print(count)
# 2. Exception Handling (5 Questions)
# Take 2 numbers from user and divide safely.
# num1 = int(input("enter"))
# num2 = int(input("eeeee"))
# try:
#     result = num1 /num2
#     print(result)
# except ZeroDivisionError:
#     print("number is not devide by zero")
# except TypeError:
#     print("numbers type zot match")

# Take age input. Handle invalid input if user enters string.
# age = input("enter age")
# try:
#     age1 = int(age)
#     print("your age is ", age1)
# except ValueError:
#     print("enter correct age make sure age is number")

# Open a file safely. If file not found show message.
try:
    file = open("data1.txt","r")
except FileNotFoundError:
    print("file not found ")
except FileExistsError:
    print("file olredy exist in memory")

# Create calculator using try-except.
while True:
    try:
        num1 = int(input("Enter first Number"))
        num2 = int(input("enter second number"))
        opp = input("what you want? \n addition press 1 \n subtraction press 2 \n multiplication press 3 \n division press 4 \n exit from calculator press 5 \n")

        if opp == "1":
            print(num1 + num2)
        elif opp == "2":
            print(num1 - num2 )
        elif opp == "3":
            print(num1*num2)
        elif opp == "4":
            print(num1 / num2)
        elif opp == "5":
            break
        else:
            pass
    except ZeroDivisionError:
        print("number is not divide by zero")
    except ValueError:
        print("enter only numbers")
    except TypeError:
        print("enter correct number")
    except Exception:
        print("something is wrong")
    # Use finally block to print "Program Ended".
    finally:
        print("Operation complated")

# 3. Decorators (5 Questions)
# Create decorator that prints "Before function call".
def decorate(fetch):
    def wrapper():
        print("Before function call")
        fetch()
        print("After function call")
    return wrapper
@decorate
def hello():
    print("Hello Function")

hello()



# Create decorator for login check.
is_login= True
def login_requred(func):
    def wrap():
        if is_login:
            print("account has been login successfully")
            func()
        else:
            print("login is requred...!")
    return wrap

@login_requred
def dashboard():
    print("Welcome to Dashboard")

dashboard()

# Create decorator to calculate execution time.
import time
def calculate(func):
    def wrap():
        start = time.time()
        func()
        end = time.time()
        print("total exicution time is ", end - start)
    return wrap

@calculate
def programs():
    for i in range(10011111):
        pass

programs()

# Create decorator that logs function name.
def logger(func):
    def wrap():
        print("function name is ", func.__name__)
        func()
    return wrap
@logger
def act():
    print("main function")

act()

# Create decorator that allows only admin user.

def validation(func):
    def wrap():
        if func.username.lower() == "admin":
            print("admin login succsessfully")
# 4. Generators (5 Questions)
# Q1

# Create generator to print numbers 1 to 10.

# Q2

# Create generator for even numbers till 20.

# Q3

# Create Fibonacci generator.

# Q4

# Create generator for squares of numbers.

# Q5

# Read large file line by line using generator.

# 5. Lambda (5 Questions)
# Q1

# Create lambda for square of number.

# Q2

# Create lambda for addition of two numbers.

# Q3

# Sort names by length using lambda.

# Q4

# Find max of two numbers using lambda.

# Q5

# Use lambda with list of dictionaries sort by salary.

# 6. Map (5 Questions)
# Q1

# Double all numbers in list using map.

# Q2

# Convert names to uppercase using map.

# Q3

# Convert string numbers to int using map.

# Q4

# Find square of each number using map.

# Q5

# Add 10 bonus to salaries using map.

# 7. Filter (5 Questions)
# Q1

# Find even numbers using filter.

# Q2

# Find odd numbers using filter.

# Q3

# Filter names starting with A.

# Q4

# Filter students with marks > 60.

# Q5

# Filter active users from list of dictionaries.

# MOST IMPORTANT INTERVIEW LEVEL COMBO QUESTIONS
# Q1

# Read file names and filter names starting with A.

# Q2

# Take user numbers → map square → filter even squares.

# Q3

# Create decorator + exception handling login system.

# Q4

# Use generator to stream file lines.

# Q5

# Use lambda to sort employees by salary.

# Real Company Asked Questions
# Python Backend Fresher
# CSV file read and insert into DB
# Handle API errors using try-except
# Create auth decorator
# Process 1 lakh records with generator
# Filter active users list
# Map response data formatting
# Best Practice for You

# Daily solve:

# 2 File Handling
# 2 Exception
# 2 Lambda/Map/Filter
# 1 Generator
# 1 Decorator


x = int(input("x"))
y = int(input("y"))
z = int(input("z"))
n = int(input("n"))
list1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(list1)

def match():
    num1 = int(input("enter num1"))
    num2 = int(input("enter num2"))
    num3 = int(input("enter num3"))
    end  = int(input("enter end"))

    list2 = [[i,j,k] for i in range(num1+1) for j in range(num2+1) for k in range(num3 +1) if i+j+k != end]
    print(list2)