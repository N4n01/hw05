def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return None
        else :
            return a / b
    else:
        return None

def main():
    while True: #A forever loop. Until "q" breaks the loop.
        try :
            a = str(input("First number (or q): "))
            if a == "q":
                break
            a = float(a)
            operator = str(input("Operator (+ - * /): "))
            b = float(input("Second number: "))

            result = calculate(a, operator, b)
            if result == None:
                print("Cannot calculate that.")
            else:
                print(f"Result: {result}")
        except ValueError :
            print("Please input real numbers only.")

main()