"""Lesson 7A Activity - Score Tracker
CS100: Roadmap to Computing

Read scores until the user types -1, then report what the loop remembered.
You don't know in advance how many scores there will be.

Expected output, typing 40, 75, 60, then -1:

    Score (-1 to stop): 40
    Score (-1 to stop): 75
    Score (-1 to stop): 60
    Score (-1 to stop): -1
    ======================
      SCORE REPORT
    ======================
    Scores:  3
    Total:   175
    Best:    75
    ======================

And typing -1 straight away:

    Score (-1 to stop): -1
    ======================
      SCORE REPORT
    ======================
    Scores:  0
    Total:   0
    Best:    0
    ======================
"""

LINE = "======================"


# TODO 1: create three memory variables BEFORE the loop:
#         count, total, best - all starting at 0
count = 0
total = 0
best = 0

# TODO 2: the priming read - ask for the first score (use int())
#         The prompt is:  "Score (-1 to stop): "
score = int(input("Score (-1 to stop): "))

# TODO 3: loop WHILE the score is not -1
while score != -1:
    total += score
    count += 1
    if score >= best:
        best = score
    score = int(input("Score (-1 to stop): "))

    # TODO 4: inside the loop:
    #           - add 1 to count
    #           - add the score to total
    #           - if the score beats best, replace best


    # TODO 5: read the NEXT score - same prompt, at the bottom of the body


# TODO 6: after the loop, print the report - once.
print(LINE)
print("    SCORE REPORT")
print(LINE)
print(f"Scores: {count}")
print(f"Total: {total}")
print(f"Best: {best}")
# ---------- TEST BEFORE YOU SUBMIT ----------
#   40, 75, 60, -1   ->  3 scores, total 175, best 75
#   -1 straight away ->  0 scores, total 0, best 0, and NO crash
#
# If it never stops, the read at the bottom of the loop is missing.
# Press Ctrl+C to get out.