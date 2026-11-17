def first_digit(s):
    for ch in s:
        if ch in "0123456789":
            return ch
    return None
print(first_digit("abc"))