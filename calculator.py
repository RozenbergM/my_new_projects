import art
print(art.logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def dev(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": dev
}


def calculator():
    should_continue = True
    n1 = float(input("Please type a number:\n"))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operator = input("Please choose a mathematical operator:\n")
        n2 = float(input("Please type the second number:\n"))
        result = operations[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        continue_or_not = input(f"Do you want to continue with {result}? print y or n:\n")
        while continue_or_not == "y":
            n1 = result
            for symbol in operations:
                print(symbol)
            operator = input("Please choose a mathematical operator:\n")
            n2 = float(input("Please type the second number:\n"))
            result = operations[operator](n1, n2)
            print(f"{n1} {operator} {n2} = {result}")
            continue_or_not = input(f"Do you want to continue with previous answer {result}? print y or n:\n")

        if continue_or_not == "n":
            print("\n" * 10)
            calculator()


calculator()
