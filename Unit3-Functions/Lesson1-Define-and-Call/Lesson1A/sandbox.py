"""Unit 3 Lesson 1A SANDBOX
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: name a block of code ----------
# Write a function called banner() that prints these three lines:
#
#   *****
#   HELLO
#   *****
#
# Then CALL it twice. You should see the banner two times.
def banner():
    print("*****")
    print("HELLO")
    print("*****")

banner()
banner()

# ---------- Quick Try 2: give it something to work with ----------
# Write show_score(name, points) so that
#     show_score("Ana", 12)
# prints:
#     Ana: 12 points
#
# Call it twice, with two different players.
def show_score(name, points):
    print(f"{name}: {points} points")

show_score("Ana", 12)
show_score("Ben", 25)

