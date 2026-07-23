try:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")