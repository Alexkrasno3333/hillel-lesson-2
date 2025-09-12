while True:
    num1 = int(input("ENTER YOUR NUMBER :"))
    num2 = int(input("ENTER YOUR NUMBER :"))
    plus = input("ENTER YOUR + - * / :")

    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2

    if plus == "+":
        print(num1 + num2)
        if result1 == num1 + num2:
            men = input("Y/N: ")
            if men == "Y":
                print("OK BRO DO AGAIN")
            else:
                break

    elif plus == "-":
        print(num1 - num2)
        if result2 == num1 - num2:
            men = input("Y/N: ")
            if men == "Y":
                print("OK BRO DO AGAIN")
            else:
                break

    elif plus == "*":
        print(num1 * num2)
        if result3 == num1 * num2:
            men = input("Y/N: ")
            if men == "Y":
                print("OK BRO DO AGAIN")
            else:
                break

    elif plus == "/":
        if num2 == 0:
            print("YOU CANT DO THIS")
        else:
            result4 = num1 / num2
            print(result4)
            if result4 == num1 / num2:
                men = input("Y/N: ")
                if men == "Y":
                    print("OK BRO DO AGAIN")
                else:
                    break




















