"""Lesson 6C Sandbox - practice file, not submitted, not graded.
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: letter by letter ----------
# Print your own first name, ONE CHARACTER PER LINE.
# Use a for-loop over the string, and print the LOOP VARIABLE.
first = False
if first:
    loop = "Jacob"
    for letter in loop:
        print(letter)
    print(loop)

# ---------- Quick Try 2: vowel counter ----------
# Ask the user for a word, then count how many vowels it has
# (a, e, i, o, u - lowercase only, that is today's rule).
# Print the count AFTER the loop, once.
#
# Remember the three places from 6B:
#   counter before the loop - update inside - use after
word = input("Enter a string: ")
vowel_count = 0
for letter in word:
    if letter in "aeiouAEIOU":
       vowel_count += 1
print(f"Vowels: {vowel_count}")

# ---------- Break it on purpose ----------
# Quick Try 2 again, but with the counter created INSIDE the loop.
# Run it with a word. Then run it again by pressing Enter (empty word).
# Write down what happened both times, and why.

# If the counter is created inside the loop, it will reset during every iteration



# ---------- Stretch (optional): reversed ----------
# Build a reversed copy of the word: put each new character on the
# LEFT of what you have so far. Start from an empty string.

reversed_word = ""
for letter in range(len(word) - 1, -1, -1):
    reversed_word += word[letter]
print(f"Reversed word: {reversed_word}")