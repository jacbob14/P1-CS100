"""Lesson 7B Activity - Guessing Game
CS100: Roadmap to Computing

The computer picks a secret number from 1 to 100. The player gets SEVEN
guesses. After each wrong guess, say "Higher" or "Lower".

random.seed(5) is already in place, so the secret is the same every run
and you can test against the expected output below. Remove that line when
you want to play for real.

Expected output, guessing 50, 75, 88, 81, 80:

    Guess (1-100): 50
    Higher
    Guess (1-100): 75
    Higher
    Guess (1-100): 88
    Lower
    Guess (1-100): 81
    Lower
    Guess (1-100): 80
    Got it in 5!

Expected output, guessing 10, 20, 30, 40, 50, 60, 70:

    Guess (1-100): 10
    Higher
    ...  (Higher after each of the first six)
    Guess (1-100): 70
    Out of guesses. It was 80.
"""

import random
random.seed(188)          # remove this line to play for real

# TODO 1: pick the secret - a random whole number from 1 to 100.
#         Careful: randint includes BOTH ends.
num = random.randint(1, 100)

# TODO 2: the priming read. Ask for the first guess, and set attempts to 1.
#         The prompt is:  "Guess (1-100): "
current_guesses = 10
guesses = 0
guess = int(input(f"{current_guesses} guesses left. Guess (1-100): "))
got_correct = True


# TODO 3: loop while the guess is wrong AND attempts is under 7.
#         Both conditions, joined with `and` - that's Lesson 3.
while guess != num:
    if guess < 1 or guess > 100:
        print("Please input a number between 1 and 100")
        guess = int(input(f"{current_guesses} guesses left. Guess (1-100): "))
        continue
    guesses += 1
    current_guesses -= 1
    if current_guesses <= 0:
        print(f"Out of guesses! The number was {num}")
        got_correct = False
        break
    print("Not Correct! Try again")
    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    guess = int(input(f"{current_guesses} guesses left. Guess (1-100): "))

if got_correct:
    print("=========")
    print(f"Correct! The number was {num}")
    print(f"Total guesses: {guesses}")

    # TODO 4: inside the loop, print "Higher" or "Lower".


    # TODO 5: read the next guess, and add 1 to attempts.


# TODO 6: after the loop, there are only two ways it could have ended.
#         Right guess   ->  Got it in N!
#         Out of guesses ->  Out of guesses. It was N.


# ---------- STRETCH (optional) ----------
# Reject guesses outside 1-100 without using up an attempt.
