input = "178416-676461"

values = input.split("-")
start = int(values[0])
end = int(values[1])


def isValidSequence(password):
    last = password[0]
    for digit in password[1:]:
        if int(digit) < int(last):
            return False
        last = digit

    return True


def containsDouble(password):
    last = password[0]
    for digit in password[1:]:
        if last == digit:
            return True
        last = digit

    return False


count = 0
for number in range(start, end):
    password = str(number)
    if isValidSequence(password) and containsDouble(password):
        count = count + 1

print(count)
