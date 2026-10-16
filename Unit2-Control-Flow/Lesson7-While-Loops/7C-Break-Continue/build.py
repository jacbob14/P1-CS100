import random
"""Lesson 7C Activity - Scoreboard
CS100: Roadmap to Computing

A tiny command loop. It keeps reading commands until the user types quit.

    +       add a point, then show the score
    -       take a point away, then show the score
    quit    stop, and show the final score
    (blank) do nothing - just ask again
    anything else: print  Use +, - or quit

Expected output, typing  +  +  (blank)  -  x  +  quit:

    > +
    Score: 1
    > +
    Score: 2
    >
    > -
    Score: 1
    > x
    Use +, - or quit
    > +
    Score: 2
    > quit
    Final score: 2
"""

# TODO 1: start the score at 0
score = 0

# TODO 2: loop forever with  while True:
print("===============")
print("Possible inputs")
print("+   ->  adds a point")
print("-  ->   substracts a point")
print("quit or q -> quits program")
while True:
    user_input = input("Enter input: ")
    
    if user_input in ("add", "+", "+1"):
        score += 1
        print(f"New Score: {score}")
    elif user_input in ("subtract", "-", "-1"):
        score -= 1
        print(f"New Score: {score} ")
    elif user_input in ("quit, q, Quit"):
        break
    elif not user_input:
        break
    else:
        continue
print(f"Program quit. Final score: {score}")

# ---------- STRETCH (optional) ----------
# Rewrite your 7B guessing game with  while True  so the guess is read once.
num = random.randint(1, 6)
while True:
    guess = int(input("Guess a number (1-100): "))
    if guess == num:
        print(f"Correct! The number was {num}")
        break
    elif guess >= num:
        print(f"Too High")
    elif guess <= num:
        print(f"Too Low")
