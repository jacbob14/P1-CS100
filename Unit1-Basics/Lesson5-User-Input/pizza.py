"""
Lesson 5 Activity: Pizza Party Splitter
CS100: Roadmap to Computing

Ask the user about their pizza order, then work out how it splits.
"""

WIDTH = 38


# --- Step 1: get the details ------------------------------------
# input() always hands you a str. Every number needs converting.
# Counts are whole numbers; a price is not.

# TODO: pizzas
pizzas = int(input("How many pizzas: "))

# TODO: slices_per_pizza
slices_per_pizza = int(input("How many slices per pizza: "))

# TODO: people
people = int(input("How many people: "))

# TODO: price_each
price_each = float((input("Price of each pizza: ")))

total_cost = pizzas * price_each

# --- Step 2: how many slices each -------------------------------
# Work out the total slices first, then split them.
# Nobody can eat 4.8 slices - which operator gives a whole number?
print(f"Each person gets {people // (pizzas * slices_per_pizza)} pizza(s)")

# --- Step 3: how many are left over -----------------------------
# After everyone takes their whole slices, some are still on the
# table. There is one operator that tells you exactly how many.
print(f"There are {people % (pizzas * slices_per_pizza)} pizza(s) left over")

# --- Step 4: the money ------------------------------------------
# Total cost, then the cost per person.
# Money should show exactly 2 decimals - use {value:.2f}.
print(f"Total cost: ${total_cost:.2f}")

# --- Step 5: the report -----------------------------------------
# Borders WIDTH wide, title centered with calculated padding.
print("=" * WIDTH)
print("             PIZZA PARTY             ")
print("=" * WIDTH)
print(f"Pizzas: {pizzas} ({pizzas * slices_per_pizza} slices total) ")
print(f"People: {people}")
print("-" * WIDTH)
print(f"Slices each: {(pizzas * slices_per_pizza) // people}")
print(f"Left over: {(pizzas * slices_per_pizza) % people}")
print(f"Total cost: ${total_cost:.2f}")
print(f"Cost each: ${price_each:.2f}")


# =============================================================
# TARGET OUTPUT
#   entering: 3 pizzas, 8 slices, 5 people, 13.99
# =============================================================
# ======================================
#              PIZZA PARTY
# ======================================
# Pizzas: 3  (24 slices total)
# People: 5
# --------------------------------------
# Slices each: 4
# Left over: 4
# Total cost: $41.97
# Cost each: $8.39
# ======================================


# =============================================================
# STRETCH (optional)
# =============================================================
# Run it again with 4 people instead of 5. The leftover count
# should change on its own. If it doesn't, you typed a number
# where a calculation belongs.