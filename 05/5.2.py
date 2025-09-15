while True:
    num1 = int(input("ENTER YOUR NUMBER :"))
    num2 = int(input("ENTER YOUR NUMBER :"))
    plus = input("ENTER YOUR + - * / :")

    if plus == "+":
        print(num1 + num2)

    elif plus == "-":
        print(num1 - num2)

    elif plus == "*":
        print(num1 * num2)

    elif plus == "/":
        if num2 == 0:
            print("YOU CANT DO THIS")
        else:
            print(num1/num2)

    men = input("yes/no ").lower()
    if men in ("y","yes"):
        print("OK BRO DO AGAIN")
    else:
        break






















