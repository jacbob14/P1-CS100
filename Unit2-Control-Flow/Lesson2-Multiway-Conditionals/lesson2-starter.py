
"""Lessons 1-2 Activity - Player Card Generator
CS100: Roadmap to Computing

Four questions in. Four decisions. One card out.

  RANK, from XP                PERK, from class
    under 500 ...... Bronze      tank ...... +50 max health
    500 to 1499 .... Silver      healer .... +20% healing
    1500 to 4999 ... Gold        scout ..... +15% move speed
    5000 and up .... Legend      anything else ... no perk

  BADGE     " *" after the username if XP is 1000 or more, otherwise nothing
  RANKED    "Eligible" if wins is 10 or more, otherwise "Not yet"

Scroll to the bottom for four complete expected outputs. Your program
must produce those exactly - same words, same spacing.
"""

LINE = "============================"


# ---------- INPUT ----------

# TODO 1: ask for the username, the class, the XP and the wins.
#         Ask in that order. XP and wins are numbers - use int().
user_name = input("Enter username: ")
user_class = input("Enter class: ")
user_XP = int(input("Enter XP: "))
user_wins = int(input("Enter wins: "))

# ---------- DECIDE ----------

# TODO 2: two NAMED BOOLEANS. Use the prefixes from Lesson 1.
#         is_veteran        -> 1000 XP or more
#         has_enough_wins   -> 10 wins or more
badge = ""
ranked = "Not Yet"
rank = ""
perk = ""
is_veteran = user_XP >= 1000
has_enough_wins = user_wins >= 10

# TODO 3: branch on is_veteran to set a badge variable.
#         Veterans get " *" (a space then a star), everyone else "".
if is_veteran:
    badge = "*"

# TODO 4: branch on has_enough_wins to set a ranked variable.
#         "Eligible" or "Not yet".
if has_enough_wins:
    ranked = "Eligible"

# TODO 5: an if / elif / else chain that sets rank from xp.
#         FOUR tiers. Check your order before you run it -
#         a player with 7500 XP must come out Legend, not Silver.
if user_XP >= 7500:
    rank = "Legend"
elif user_XP >= 5000:
    rank = "Gold"
elif user_XP >= 2500:
    rank = "Silver"
elif user_XP >= 1000:
    rank = "Bronze"
else:
    rank = "Not ranked"

# TODO 6: an if / elif / else chain that sets perk from the class.
#         This one compares text with == instead of numbers.
#         End it with an else so an unknown class still gets something.
if user_class == "one":
    perk = "+20% healing"
if user_class == "two":
    perk = "+40% shield"
if user_class == "three":
    class_id = "+20% strength"
if user_class == "four":
    class_id = "+50% movement"

# ---------- SHOW ----------

# TODO 7: print the card. print(LINE) for the ==== lines, f-strings for
#         the rest. Print it ONCE, after all the deciding is done.
#         The labels are padded so the values line up - copy the
#         spacing from the expected output below exactly.
print(LINE)
print("       PLAYER CARD       ")
print(LINE)
print(f"User: {user_name}")
print(f"Class: {user_class}")
print(f"XP: {user_XP}")
print(f"Perk: {perk}")
print(f"{ranked}")
print(LINE)
# =====================================================================
#  EXPECTED OUTPUT - run all four before you submit
# =====================================================================
#
#  RUN 1   nova / healer / 7500 / 12
#
#     ============================
#            PLAYER CARD
#     ============================
#     User:   nova *
#     Class:  healer
#     XP:     7500
#     Rank:   Legend
#     Perk:   +20% healing
#     Ranked: Eligible
#     ============================
#
#
#  RUN 2   ace / tank / 500 / 3
#          exactly 500 - the Silver edge. No badge, not ranked.
#
#     ============================
#            PLAYER CARD
#     ============================
#     User:   ace
#     Class:  tank
#     XP:     500
#     Rank:   Silver
#     Perk:   +50 max health
#     Ranked: Not yet
#     ============================
#
#
#  RUN 3   rex / scout / 1500 / 10
#          exactly 1500 and exactly 10 wins - two edges at once.
#
#     ============================
#            PLAYER CARD
#     ============================
#     User:   rex *
#     Class:  scout
#     XP:     1500
#     Rank:   Gold
#     Perk:   +15% move speed
#     Ranked: Eligible
#     ============================
#
#
#  RUN 4   zed / mage / 200 / 0
#          "mage" is not a real class - your else has to catch it.
#
#     ============================
#            PLAYER CARD
#     ============================
#     User:   zed