"""
Lesson 3A Activity: Tournament Banner
CS100: Roadmap to Computing

Build the banner shown at the bottom of this file.

Everything you need is from today: print(), commas, sep, end, the *
operator, len(), and quote handling. No f-strings - those are next class.

Work top to bottom. Run after every step.
    Right-click in this file -> "Run Python File in Terminal"

Save before you run. Commit and push when your output matches.
"""

WIDTH = 40
title = "BERGEN TECH OPEN"


# --- Step 1: loading line -------------------------------------
# Two print() calls, ONE line of output.
#   Loading bracket... done
print("Loading bracket...")
print("Done")


# --- Step 2: header block -------------------------------------
# A border WIDTH wide, the title centered, then another border.
# Calculate the padding from WIDTH and len(title) - don't count
# spaces by hand. Use // so you get a whole number.
padding = WIDTH - len(title)

# --- Step 3: rounds line --------------------------------------
# Careful: sep goes between EVERY pair, so "Rounds:" would get one
# too. Print the label first with end=" ", then let a second print
# handle the sep.
#   Rounds: Round 1 > Round 2 > Finals
print("Round1 Round2 Finals", sep = ">")


# --- Step 4: format line --------------------------------------
# Same trap, different fix. This time use ONE print() and fold the
# label into the first item.
#   Format: 8 teams / 7 matches / 2 days
print("8 teams 7 matches 2 days", sep = "/")

# --- Step 5: the quote ----------------------------------------
# This line has a double quote AND an apostrophe, so switching the
# outer quote won't save you on its own.
#   Coach said "let's play".
print("let's play", end = '')
print('"')

# --- Step 6: closing border -----------------------------------


# =============================================================
# TARGET OUTPUT
# =============================================================
# Loading bracket... done
#
# ========================================
#             BERGEN TECH OPEN
# ========================================
# Rounds: Round 1 > Round 2 > Finals
# Format: 8 teams / 7 matches / 2 days
#
# Coach said "let's play".
#
# ========================================
print("Loading bracket... done")
print(" ")
print("========================================")
print("            BERGEN TECH OPEN           ")
print("========================================")
print("Round > Round 2 > Finals")
print("Format: 8 teams / 7 matches / 2 days")
         
# =============================================================
# STRETCH (optional)
# =============================================================
# Change title to your own name. The banner must still center it
# correctly. If it doesn't, you hard-coded the padding.