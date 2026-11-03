"""Unit 3 Lesson 1B SANDBOX
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: send it back ----------
# Write format_handle(username) that RETURNS the username with @ in front.
# Don't print inside the function. Then use what it returns:
#
#     print(f"Follow {format_handle('nasa')} today")
#
# should print:
#     Follow @nasa today
def format_handle(username):
    return f"@{username}"

print(f"Follow {format_handle('nasa')} today")

# ---------- Quick Try 2: fix the trap ----------
# This should return the whole word, but it returns only the first letter.
# Run it, then fix it by moving ONE line.

def build(word):
    result = ""
    for ch in word:
        result = result + ch
    return result

print(build("dog"))     # should print: dog
