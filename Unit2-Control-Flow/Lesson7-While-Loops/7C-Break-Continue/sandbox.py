"""Lesson 7C SANDBOX
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: write the input ONCE ----------
# This is the 7A sentinel sum. The input line appears twice.
# Rewrite it with  while True:  and  break  so input() appears ONCE.
# It should still print the same total.

# total = 0
# num = int(input("Number (0 to stop): "))
# while num != 0:
#     total = total + num
#     num = int(input("Number (0 to stop): "))
# print(f"Total: {total}")

total = 0
while True:
    num = int(input("Number (0 to stop): "))
    if num == 0:
        print("Found 0, exiting loop")
        break


# ---------- Quick Try 2: skip some ----------
# Print the numbers 1 to 10, but skip 3 and 7.
# Use  continue.

while True:
    num = int(input("Enter a number: "))
    if not num:
        print("exiting loop")
        break
    if num == 3 or num == 7:
        continue
    print(num)
    
    
