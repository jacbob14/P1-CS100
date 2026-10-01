"""Lesson 6A Sandbox
CS100: Roadmap to Computing
"""

print(range(5))
# ---------- Quick Try 1: what does range give you? ----------



# ---------- Quick Try 2: the loop variable is real ----------
# Print the round number and the damage for each round.
# Damage is 10 times the round number.
#
# Careful: range(4) starts at 0, but there is no "Round 0".
damage = 100
damage_per_round = 10
round_number = 10

# ---------- Try it: inside or outside? ----------
# Move the "Match over" line so it prints ONCE, at the end.
# Then move it back so it prints after every round.
# What is the only thing you changed?
for round in range(1, round_number):
    print(f"Round #{round}. Damage done: {damage - round * damage_per_round}")
print("Match over")

for i in range(3):
    print("Fighting...")
    print("Match over")
