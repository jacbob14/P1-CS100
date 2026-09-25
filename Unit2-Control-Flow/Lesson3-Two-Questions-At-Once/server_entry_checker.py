"""Lesson 3 Activity - Server Entry Checker
CS100: Roadmap to Computing

Four questions in. One entry pass out.

  STATUS     "Blocked" if the player is banned OR has no username,
             otherwise "Allowed"
  RANKED     "Eligible" if 1000 XP or more AND 10 wins or more,
             otherwise "Not yet"
  ACTIVE     "Yes" if wins is above zero, otherwise "No"

Scroll to the bottom for three complete expected outputs.
"""

LINE = "============================"


# ---------- INPUT ----------

# TODO 1: ask for the username, the XP, the wins, and whether the
#         player is banned (expect "y" or "n").
#         XP and wins are numbers - use int().
username = input("Enter username: ")
xp = int(input("Enter XP: "))
wins = int(input("Enter wins: "))
banned_input = input("Banned: ")

# ---------- DECIDE ----------

# TODO 2: two named booleans for the ranked rule.
#         is_veteran        -> 1000 XP or more
#         has_enough_wins   -> 10 wins or more
is_veteran = xp >= 1000
has_enough_wins = wins >= 10

# TODO 3: can_play_ranked - BOTH of those must be true.
can_play_ranked = is_veteran and has_enough_wins

# TODO 4: is_banned      -> the answer was "y"
#         is_blocked     -> banned OR the username is empty
#         Use a truthiness check for the empty username.
is_banned = banned_input == "y"
is_blocked = is_banned or not username

# TODO 5: is_active -> wins is above zero.
#         Careful: use > 0 here, not a truthiness check.
#         Zero wins is real data.
is_active = wins > 0

# ---------- SHOW ----------

# TODO 6: use if / else to turn each boolean into its word, then
#         print the pass ONCE, after all the deciding is done.
print(LINE)
print("    SERVER ENTRY PASS    ")
print(LINE)
if username:
    print(f"Username: {username}")
    
if is_blocked:
    print("Status: Blocked")
elif not is_blocked:
    print("Status: Allowed")
    
if can_play_ranked:
    print("Ranked: Eligible")
elif not can_play_ranked:
    print("Ranked: Ineligible")

if is_active:
    print("Active: Yes")
elif not is_active:
    print("Active: No")
# =====================================================================
#  EXPECTED OUTPUT
# =====================================================================
#
#  RUN 1   nova / 1450 / 12 / n
#
#     ============================
#         SERVER ENTRY PASS
#     ============================
#     User:    nova
#     Status:  Allowed
#     Ranked:  Eligible
#     Active:  Yes
#     ============================
#
#
#  RUN 2   ace / 1450 / 3 / n
#          Enough XP, not enough wins. `and` needs both.
#
#     ============================
#         SERVER ENTRY PASS
#     ============================
#     User:    ace
#     Status:  Allowed
#     Ranked:  Not yet
#     Active:  Yes
#     ============================
#
#
#  RUN 3   (blank username) / 200 / 0 / y
#          Banned AND no username - either one alone blocks them.
#
#     ============================
#         SERVER ENTRY PASS
#     ============================
#     User:    unnamed
#     Status:  Blocked
#     Ranked:  Not yet
#     Active:  No
#     ============================
#
# =====================================================================
#  ALSO TEST
# =====================================================================
#     nova / 1450 / 12 / y    -> Blocked, but still Ranked Eligible
#     blank  / 9999 / 99 / n  -> Blocked on the username alone
#
#  If your `or` is wrong, one of those two will come out Allowed.
# =====================================================================