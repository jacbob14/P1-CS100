"""Unit 3 Lesson 2B Activity - Username Checker
CS100: Roadmap to Computing

Write four functions that take a STRING and RETURN an answer.
Don't print inside them.

Expected output:

    @nasa
    2
    True
    False
    AL

Rubric:
    1. Every function returns its answer - nothing printed inside
    2. clean_handle uses string methods and returns the NEW string
    3. has_digit returns True INSIDE the loop (the one time that is right)
       and False AFTER it
    4. initials builds a new string: result = "" BEFORE the loop,
       return AFTER it

Stretch (only when the four above work): is_valid, at the bottom.
"""


def clean_handle(text):
    """Return text without spaces at the ends, in lower case, with @ in front."""
    # Hint: text.strip() and text.lower() each give back a NEW string
    pass


def count_vowels(name):
    """Return how many vowels (a, e, i, o, u) are in name."""
    count = 0
    for ch in name:
        pass        # TODO: if ch is a vowel, add 1 to count
    # TODO: return count - AFTER the loop


def has_digit(name):
    """Return True if name contains a digit 0-9, otherwise False."""
    for ch in name:
        pass        # TODO: if ch is a digit, return True right away
    # TODO: return False - AFTER the loop


def initials(full_name):
    """Return the capital first letters of each word: "ada lovelace" -> "AL"."""
    # Hint: result = "" first. Loop over full_name.split().
    # Add part[0].upper() each time. Return AFTER the loop.
    pass


# ---------- TESTS - don't change anything below this line ----------
print(clean_handle("  NASA "))
print(count_vowels("netflix"))
print(has_digit("tswift13"))
print(has_digit("nasa"))
print(initials("ada lovelace"))


# ---------- STRETCH ----------
# is_valid(name) returns True only if name has at least 3 characters
# AND contains no spaces. Hint: len(name) >= 3 and " " not in name
# def is_valid(name):
#     ...
# print(is_valid("ab"))          # False
# print(is_valid("my name"))     # False
# print(is_valid("nasa"))        # True
