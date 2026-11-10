"""Unit 3 Lesson 2A SANDBOX
CS100: Roadmap to Computing

Do these in order. Type each line yourself - don't copy and paste.
"""

# ---------- Code Along 1: look inside a list ----------
likes = [500, 1200, 800]
print(likes)                # [500, 1200, 800]
print(len(likes))           # 3
print(likes[0])             # 500   the FIRST item is index 0
print(likes[-1])            # 800   index -1 is the LAST item

# YOUR TURN: add three lines that print
#   the middle like        -> 1200
#   the first two likes    -> [500, 1200]    (a slice)
#   the last two likes     -> [1200, 800]    (a slice with a negative start)
print(likes[1])
print(likes[:2])
print(likes[-2:])


# ---------- Code Along 2: change a list ----------
handles = ["@nasa", "@tswift", "@netflix"]
handles.append("@cnn")
handles[0] = "@bbc"
print(handles)              # ['@bbc', '@tswift', '@netflix', '@cnn']

# YOUR TURN: append "@espn", then print how many handles there are  -> 5
handles.append("@espn")
print(len(handles))


# ---------- Code Along 3: loop over a list (if you finish early) ----------
# Print every handle on its own line, using a for loop.
for handle in handles:
    print(handle)
