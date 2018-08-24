try:

    a = input('type a number:')
    b = input('input another:')
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    # print("b cannot be zero.")
    print("Invalid input.")
