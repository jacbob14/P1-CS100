"""Lesson 3 Sandbox
CS100: Roadmap to Computing`
"""

# ---------- Quick Try: combine conditions ----------
xp = 1450
wins = 12
is_banned = False

is_veteran = xp >= 1000
has_enough_wins = wins >= 10

# can_play_ranked   -> 1000 XP or more AND 10 wins or more
can_play_ranked = is_veteran and has_enough_wins
# is_new_player     -> under 100 XP OR no wins at all
is_new_player = xp < 100 or not wins
# can_post          -> NOT banned
can_post = not is_banned
# Print all three with f-strings and look at the answers.
print(f"Can play ranked: {can_play_ranked}")
print(f"Is new player: {is_new_player}")
print(f"Can post: {can_post}")

# ---------- Predict, then run: truthiness ----------
# Write your prediction BEFORE you run anything.
# Which letters print?   My prediction: ______

username = ""
clan = "Nova"
coins = 0

# if username is truthy, print "A"
if username: print("A")
# if clan is truthy, print "B"
if clan: print("B")
# if coins is truthy, print "C"
if coins: print("C")
# Now run it. Did your prediction match?
