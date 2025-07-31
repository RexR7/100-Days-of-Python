import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

stored_values = {"+":add, "-":sub, "*":mul, "/":div}

def calc():
    first_number = int(input("What's the first number? "))
    for key in stored_values:
        print(key)
    operation_choice = str(input('''Pick an operation: '''))
    second_number = int(input("What's the second number? "))

    result = stored_values[operation_choice](first_number, second_number)
    print(f"{first_number} {operation_choice} {second_number} = {result}")

    while True:
        continue_calc = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. ").strip().lower())
        if continue_calc == "y":
            for key in stored_values:
                print(key)
            operation_choice = input("Pick an operation: ")
            next_number = int(input("What's the next number? "))
            new_result = stored_values[operation_choice](result, next_number)
            print(f"{result} {operation_choice} {next_number} = {new_result}")
        elif continue_calc == "n":
            print("\nStarting new calculation...\n")
            print("\n"* 100)
            return calc()
        else:
            print(str(input(f"Invalid Response. {continue_calc}")))
calc()