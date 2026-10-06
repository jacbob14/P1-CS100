"""Lesson 6C Activity - Text Analyzer
CS100: Roadmap to Computing

Ask the user for a line of text, then report how many vowels,
consonants, digits, spaces, and other characters it contains -
in ONE pass through the text.

Expected output:

    Enter text: code 4 u
    ================
      TEXT ANALYZER
    ================
    Vowels:     3
    Consonants: 2
    Digits:     1
    Spaces:     2
    Other:      0
    ================

Rubric:
    1. Five counters created BEFORE the loop
    2. One for-loop over the text - a single pass
    3. An if / elif chain: vowels first, then a-z, then 0-9,
       then space, then else
    4. Report printed once, AFTER the loop
"""

LINE = "================="

# TODO 1: Ask the user for a line of text and store it in `text`.
text = input("Enter test: ")
# TODO 2: Create five counters, all starting at 0:
#         vowels, consonants, digits, spaces, other
vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0
other = 0
    

# TODO 3: Loop over the text, one character at a time.
for letter in text:
    if letter in "aeiouAEIOU":
        vowel_count += 1
    elif letter in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRTTVWXYZ":
        consonant_count += 1
    elif letter in "0123456789":
        digit_count += 1
    elif letter == " ":
        space_count += 1
    else:
        other += 1
print(LINE)
print("  TEXT ANALYZER")
print(LINE)
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
print(f"Other characters: {other}")
print(LINE)

    # TODO 4: if the character is a vowel, count it as a vowel.
    # TODO 5: elif it is a lowercase letter, count it as a consonant.
    # TODO 6: elif it is a digit, count it as a digit.
    # TODO 7: elif it is a space, count it as a space.
    # TODO 8: otherwise, count it as other.


# TODO 9: Print the report - header, five counts, footer - once.
