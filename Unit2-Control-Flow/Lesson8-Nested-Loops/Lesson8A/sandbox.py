"""Lesson 8A SANDBOX
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: a grid of # ----------
# Print 3 rows of 5 # signs, using a loop inside a loop.
# Use  print("#", end="")  for each sign, and  print()  to end each row.
#
#   #####
#   #####
#   #####


# ---------- Quick Try 2: a times table ----------
# Print the 5 x 5 times table. Each row is one number times 1 to 5.
# Use  print(row * col, end=" ")  inside, and  print()  after the inner loop.
col = 5
row = 5
for row in range(1, row):
    for col in range(1, col):
        print(row * col, end = " ")
    print()
            
        
    
    
        
        