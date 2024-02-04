def dix_bag():
    try:
        num = float(input("Input a number: "))

        print("You input:", num)

    except ValueError:

        print("Error: this is not a number.")
