def roundFunction(inputNumber):
    # extreme example of
    #  - how to use variables at each step
    #  - how to print out values at every point to understand what's happening inside your function

    print("roundFunction started")
    print("inputNumber", inputNumber)

    decimalPointMoved = inputNumber * 10

    decimalPlaces = decimalPointMoved % 1
    print("decimalPlaces", decimalPlaces)

    if decimalPlaces < 0.5:
        print("case 1 < 0.5")

        removeDecimalPoint = decimalPointMoved//1
        decimalPointMovedBack = removeDecimalPoint/10

        print("decimalPointMoved", decimalPointMoved)
        print("removeDecimalPoint", removeDecimalPoint)
        print("decimalPointMovedBack", decimalPointMovedBack)

        return decimalPointMovedBack
    else:
        print("case 2 else >= 0.5")

        removeDecimalPoint = decimalPointMoved//1
        roundedNumber = removeDecimalPoint + 1
        decimalPointMovedBack = roundedNumber/10

        print("removeDecimalPoint", removeDecimalPoint)
        print("roundedNumber", roundedNumber)
        print("decimalPointMovedBack", decimalPointMovedBack)


roundFunction(3.25)
