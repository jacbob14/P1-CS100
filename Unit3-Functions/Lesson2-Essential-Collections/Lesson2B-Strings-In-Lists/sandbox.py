"""Unit 3 Lesson 2B SANDBOX
CS100: Roadmap to Computing

Do these in order. Type each line yourself - don't copy and paste.
"""

# ---------- Code Along 1: a string is a sequence ----------
word = "python"
print(word[0])              # p     the FIRST letter is index 0
print(word[-1])             # n     index -1 is the LAST letter
print(word[1:4])            # yth   the stop is NOT included
print(len(word))            # 6

# YOUR TURN: add two lines that print
#   the first three letters   -> pyt
#   the last two letters      -> on


# ---------- Code Along 2: methods give you a NEW string ----------
name = "  Ada Lovelace  "
print(name.strip())                       # Ada Lovelace
print(name.strip().lower())               # ada lovelace
print(name.strip().replace("a", "A"))     # AdA LovelAce
print(len(name))                          # 16   name itself never changed

# YOUR TURN: split the stripped name into a list and print how many
# words there are  -> 2


# ---------- Code Along 3: count (if you finish early) ----------
# Use .count to print how many times "a" appears in "banana"   -> 3
