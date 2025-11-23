def add(a, b):
    return a + b

def mul(a, b):
   return a * b


print("*\n --- Simple Calculater ---")
print("1. ADD")
print("2. MULTIPLY")

choice = input("Enter your choice")

num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
if choice == '1':
    print("Result", add(num1, num2))

elif choice == '2':
     print("Result", mul(num1, num2))

else:
    print("invalid choice try again" )