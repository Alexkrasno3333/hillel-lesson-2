import keyword
import string

print_text = input("Enter your text: ")

underscores = 0
has_upper = 0
invalid_char = 0

if not print_text:
    print("FALSE")

elif print_text == "_":
    print("TRUE")

elif all(ch == "_" for ch in print_text):
    print("FALSE")

else:
    for char in print_text:
        if char.isupper():
            has_upper = 1

        if char in string.punctuation and char != "_":
            invalid_char = 1
        if char == " ":
            invalid_char = 1

        if char == "_":
            underscores += 1

    if has_upper:
        print("FALSE")

    elif print_text[0].isdigit():
        print("FALSE")

    elif invalid_char:
        print("FALSE")

    elif print_text in keyword.kwlist:
        print("FALSE")

    else:
        print("TRUE")













