"""Lesson 4 Activity - Refactor the Badge Maker
CS100: Roadmap to Computing

This program already works. Do not change what it prints.

Six blocks below decide six values. FIVE of them are simple two-way
choices and should become one-line ternaries. ONE of them is not -
leave that one alone and write a comment saying why.

Run it once before you touch anything, and save the output. When you
are done, run it again. The two must be identical.
"""

username = input("Username: ")
xp = int(input("XP: "))
wins = int(input("Wins: "))
is_banned = input("Banned? (y/n): ") == "y"


# ---------- BLOCK 1 ----------
# if xp >= 1000:
#     badge = " *"
# else:
#     badge = ""
badge = " *" if xp >= 1000 else ""

# ---------- BLOCK 2 ----------
# if username:
#     display_name = username
# else:
#     display_name = "Guest"
display_name = username if username else "Guest"

# ---------- BLOCK 3 ----------
# if wins == 1:
#     win_word = "win"
# else:
#     win_word = "wins"
win_word = "win" if wins == 1 else win_word = "wins"

# ---------- BLOCK 4 ----------
# if xp >= 5000:
#     rank = "Legend"
# elif xp >= 1500:
#     rank = "Gold"
# elif xp >= 500:
#     rank = "Silver"
# else:
#     rank = "Bronze"
rank = "Legend" if xp >= 5000 else "Gold" if xp >= 1500 else "Silver" if xp >= 500 else "Bronze"

# ---------- BLOCK 5 ----------
# if is_banned:
#     status = "Blocked"
# else:
#     status = "Allowed"
status = "Blocked" if is_banned else "Allowed"

# ---------- BLOCK 6 ----------
# if wins > 0:
#     activity = "Active"
# else:
#     activity = "New"
activity = "Active" if wins > 0 else "New"

# ---------- OUTPUT - do not change ----------
LINE = "============================"
print(LINE)
print("       BADGE MAKER")
print(LINE)
print(f"User:   {display_name}{badge}")
print(f"Rank:   {rank}")
print(f"Record: {wins} {win_word}")
print(f"Status: {status}")
print(f"Play:   {activity}")
print(LINE)


# =====================================================================
#  EXPECTED OUTPUT - must be the same before and after your refactor
# =====================================================================
#
#  RUN 1   nova / 7500 / 12 / n
#
#     ============================
#            BADGE MAKER
#     ============================
#     User:   nova *
#     Rank:   Legend
#     Record: 12 wins
#     Status: Allowed
#     Play:   Active
#     ============================
#
#
#  RUN 2   (blank) / 300 / 1 / y
#          One win, no username, banned, bottom rank.
#
#     ============================
#            BADGE MAKER
#     ============================
#     User:   Guest
#     Rank:   Bronze
#     Record: 1 win
#     Status: Blocked
#     Play:   Active
#     ============================
#
#
#  RUN 3   ace / 1500 / 0 / n
#          Exactly 1500 - a boundary. Zero wins.
#
#     ============================
#            BADGE MAKER
#     ============================
#     User:   ace *
#     Rank:   Gold
#     Record: 0 wins
#     Status: Allowed
#     Play:   New
#     ============================
#
# =====================================================================
#  RULES
# =====================================================================
#   - Five blocks become one-line ternaries.
#   - One block stays exactly as it is. Add a comment above it saying
#     why a ternary is the wrong tool for that one.
#   - No nested ternaries. If you find yourself writing a second
#     `else` on the same line, that is the block you should have left.
#   - Every ternary fits on one line without wrapping.
# =====================================================================
