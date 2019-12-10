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


def findGroupLength(number, digit):
    index = number.index(digit) + 1

    groupLength = 1
    while index < len(number) and number[index] == digit:
        groupLength += 1
        index += 1

    return groupLength


def containsDouble(password):
    for digit in set(password):
        length = findGroupLength(password, digit)
        if length == 2:
            return True

    return False


count = 0
for number in range(start, end):
    password = str(number)
    if isValidSequence(password) and containsDouble(password):
        count = count + 1

print(count)

