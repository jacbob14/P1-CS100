"""Lesson 6B Activity - Session Report
CS100: Roadmap to Computing

Loop through the rounds of a training session and report three things
the loop had to REMEMBER.

  Damage for round N is N * 10.
  A round counts as a BIG HIT when its damage is 30 or more.

Your output for 4 rounds:

    ========================
      SESSION REPORT
    ========================
    Round 1 - 10 damage
    Round 2 - 20 damage
    Round 3 - 30 damage
    Round 4 - 40 damage
    ========================
    Total damage: 100
    Big hits:     2
    Best round:   40
    ========================

And for 2 rounds:

    ========================
      SESSION REPORT
    ========================
    Round 1 - 10 damage
    Round 2 - 20 damage
    ========================
    Total damage: 30
    Big hits:     0
    Best round:   20
    ========================
"""

LINE = "========================"


# TODO 1: ask how many rounds, convert with int()
rounds = int(input("Number of rounds: "))

# TODO 2: create your three memory variables, BEFORE the loop.
#         total     -> starts at 0
#         big_hits  -> starts at 0
#         best      -> starts at 0
#
#         Every one of these has to survive between runs of the loop.
#         If you create them inside, they get wiped every time.
total = 0
big_hits = 0
best = 0

# TODO 3: print the header - LINE, title, LINE. Once.
print(LINE)
print("  SESSION REPORT")
print(LINE)

# TODO 4: loop once per round. Inside the loop:
#           - work out this round's damage  (round number * 10)
#           - print the round line
#           - ADD the damage to total
#           - if the damage is 30 or more, add 1 to big_hits
#           - if the damage beats best, replace best
for i in range(1, rounds + 1):
    print(f"Round {i} - {i * 10} damage")
print(LINE)
for i in range(1, rounds + 1):
    total += i * 10
    if total >= 30:
        big_hits += 1
    if i * 10 > best:
        best = i * 10
print(f"Total damage: {total}")
print(f"Big hits: {big_hits} ")
print(f"Best round: {best}")
    

# TODO 5: after the loop, print LINE and the three totals, then LINE.
#         These print ONCE.


# ---------- TEST BEFORE YOU SUBMIT ----------
#   4 rounds -> total 100, big hits 2, best 40
#   2 rounds -> total 30,  big hits 0, best 20
#   0 rounds -> total 0,   big hits 0, best 0, and NO crash
#
# If your totals come out as just the last round's damage, one of your
# memory variables is in the wrong place.
