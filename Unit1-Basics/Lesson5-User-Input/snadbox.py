"""
Lesson 5 SANDBOX
CS100: Roadmap to Computing
"""


# =============================================================
# QUICK TRY 1 — input() and conversion
# =============================================================
# Run this. Type a number when it asks. Then read the error.

# age = input("Your age: ")
# print(age + 1)


# TODO: fix the line above so it prints your age plus one.
age = int(input("Your age: "))
print(age + 1)

# TODO: ask for a price and convert it properly.
#       A price is not a whole number.
price = float(input("Price: "))
print(f"Price: ${int(price)}")

# =============================================================
# QUICK TRY 2 — operators
# =============================================================
# Predict each answer BEFORE you run it.

print(17 / 5) # 3.4
print(17 // 5) # 3
print(17 % 5) # 2
print(2 ** 5) # 32


# TODO: 17 slices, 5 people. Print how many each person gets
#       and how many are left over.
print("17 slices, 5 people")
print(f"Each person gets {17 // 5} slices, with {17 % 5} slices left over.")

# TODO: predict this one, then run it. It surprises people.
# print(-7 % 3)
print(-7 % 3) # 2