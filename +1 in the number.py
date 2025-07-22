def plus_one(digits):
    i = len(digits) - 1
    carry = 1

    while i >= 0:
        number = digits[i] + carry
        if number < 10:
            digits[i] = number
            carry = 0
            break
        else:
            digits[i] = 0
            carry = 1
        i -= 1

    if carry == 1:
        digits.insert(0, 1)
    return digits
