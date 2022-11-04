from art import print_display

from calFuncs import operations, format_operations, single_num_operations


def main():
    while (True):
        print_display()

        num1 = float_input("Enter a number: ")
        history = f"{num1}"
        print_display(num1, "")

        while (True):
            opt = opt_input()

            if opt == "ac" or opt == "c":
                break
            if opt in single_num_operations:
                answer = calculate_single_num(num1, opt)
                history = format_operations[opt](history)
            else:
                # to show the chosen operation before num2 provided by user
                print_display(num1, opt)
                # after num2 input, answer calculated and display history prepared
                num2 = float_input("Enter a number: ")
                answer = calculate(num1, num2, opt)
                history = format_operations[opt](history, num2)

            print_display(history, f"= {answer}")
            num1 = answer


def calculate_single_num(n1, opt):
    calFunc = operations[opt]
    return calFunc(n1)


def calculate(n1, n2, opt):
    calFunc = operations[opt]
    return calFunc(n1, n2)


def float_input(promptStr):
    while True:
        try:
            n = float(input("Enter a number: "))
        except:
            print("", end="")
        else:
            return n


def opt_input():
    print("\nOperations: AC ", end="")
    validOpts = []
    for o in operations:
        validOpts.append(o)
        print(f", {o} ", end="")
    print("\n")

    while True:
        opt = input("Pick an operation: ").strip().lower()
        if opt in validOpts or opt == "ac" or opt == "c":
            return opt


if __name__ == '__main__':
    main()
