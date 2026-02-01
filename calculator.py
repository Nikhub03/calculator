def processes(a, b, c):
    if c == "+":
        print(f"\nResult {a + b}\n")
    elif c == "-":
        print(f"\nResult: {a - b}\n")
    elif c == "/":
        print(f"\nResult {a / b}\n")
    elif c == "*":
        print(f"\nResult: {a * b}\n")

def menu():
    print('''\nConsole Calculator
==============================
1. Run
2. Stop\n''')

def main():
    while True:
        menu()
        n = int(input("Enter process (1 or 2): "))
        if n == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            c = str(input("Enter process (+, -, /, *): "))
            processes(a, b, c)
        elif n == 2:
            print("Stop programm!\n")
            break
        else:
            print("Error")

if __name__ == "__main__":
    main()