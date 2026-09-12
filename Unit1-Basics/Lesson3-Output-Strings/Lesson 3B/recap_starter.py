"""
Lesson 3B Activity: Match Recap Card
CS100: Roadmap to Computing

Build the recap card shown at the bottom of this file.

New today: f-strings, escape sequences, triple quotes.
Also reuses Part A: sep, end, and the * operator.

Work top to bottom. Run after every step.
Save before you run. Commit and push when your output matches.
"""

player = "Nova"
rank = "Diamond II"
agent = "Jett"
rounds_won = 13
rounds_lost = 9
kills = 24
deaths = 11
assists = 7
accuracy = 44
game_map = "Ascent"
minutes = 42
WIDTH = 40


# --- Step 1: header block -------------------------------------
# Border, centered title, border. The title is below.
# Calculate the padding - don't count spaces.
title = "MATCH RECAP - VALORANT"


# --- Step 2: player line --------------------------------------
# ONE print() using sep=" | ". Each item is its own f-string.
#   Player: Nova | Rank: Diamond II | Agent: Jett
print(f"Nova | Rank: {rank} | Agent: {agent}")

# --- Step 3: stats lines --------------------------------------
# Rounds uses sep=" > ", K/D/A uses sep=" / ".
# Remember the label trap from last class.
#   Rounds: 13 > 9
#   K/D/A: 24 / 11 / 7
print(f"Rounds: {rounds_won}", f"{rounds_lost}", sep=' > ')

# --- Step 4: accuracy bar -------------------------------------
# A 10-character bar: # for filled, . for empty.
# CALCULATE the filled count from accuracy - do not type the bar
# out by hand. Use // and the * operator, then put both halves
# inside one f-string.
#   Accuracy: ########.. 82%
first = "#" * (accuracy // 10)
last = "." * (10 - (int(len(first))))
print(first, last, " ", accuracy, "%")


# --- Step 5: the quote ----------------------------------------
# Both quote types appear, and it needs the player's name inserted.
#   Nova said, "that's my best game."
print("""that's my best game.""")

# --- Step 6: notes block --------------------------------------
# ONE triple-quoted f-string producing every line below, including
# the blank line above "Match Notes:" and the closing border.
# The three indented lines use a TAB escape, not spaces.
# Reminder: triple quotes alone do NOT substitute variables.
#   (blank line)
#   Match Notes:
#       Map: Ascent
#       Duration: 42 min
#       MVP: yes
#   ========================================
print(f"""
Match Notes:
    Map: {game_map}
    Duration: {minutes} min
    MVP: yes
""")

# =============================================================
# TARGET OUTPUT
# =============================================================
# ========================================
#          MATCH RECAP - VALORANT
# ========================================
# Player: Nova | Rank: Diamond II | Agent: Jett
#
# Rounds: 13 > 9
# K/D/A: 24 / 11 / 7
# Accuracy: ########.. 82%
#
# Nova said, "that's my best game."
#
# Match Notes:
#     Map: Ascent
#     Duration: 42 min
#     MVP: yes
# ========================================
# (the three indented lines are TABS in your output, not spaces)


# =============================================================
# STRETCH (optional)
# =============================================================
# Change player, rank, accuracy, and minutes at the top.
# The card must still line up and the bar must still be 10
# characters. If something breaks, you hard-coded a value you
# should have calculated.