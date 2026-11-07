def check_number(num):
    if num > 0:
        return "Positive Number"
    elif num < 0:
        return "Negative Number"
    else:
        return "Zero"


if __name__ == "__main__":
    num = float(input("Enter a number: "))
    print(check_number(num))