"""Unit 3 Lesson 2A Activity - Post Stats
CS100: Roadmap to Computing

You have the daily like counts for one post. Write three functions that take
the LIST and RETURN an answer. Don't print inside them.

Expected output:

    Total: 4600
    Average: 920
    Last three: [800, 1500, 600]

Rubric:
    1. Every function returns its answer - nothing printed inside
    2. average_likes CALLS total_likes instead of adding everything again
    3. last_three uses a slice

Stretch (only when the three above work): trending_days, at the bottom.
"""


def total_likes(likes):
    """Return the sum of all the like counts."""
    total = 0
    for like in likes:
        total += like
    return total


def average_likes(likes):
    """Return the whole-number average of the like counts."""
    # Hint: call total_likes(likes), then divide by len(likes) using //
    return total_likes(likes) // len(likes)


def last_three(likes):
    """Return the last three like counts, as a new list."""
    # Hint: a slice that starts three from the end
    return likes[-3:]


# ---------- TESTS - don't change anything below this line ----------
likes = [500, 1200, 800, 1500, 600]
print("Total:", total_likes(likes))
print("Average:",   average_likes(likes))
print("Last three:", last_three(likes))


# ---------- STRETCH ----------
# trending_days(likes, limit) returns a NEW list holding only the like
# counts above limit. For the list above and a limit of 1000 it should
# give [1200, 1500].
# Hint: start with result = [] BEFORE the loop, append inside the loop,
# and return AFTER the loop.
def trending_days(likes, limit):
    """Return a new list holding only the like counts above limit."""
    result = []
    for like in likes:
        if like > limit:
            result.append(like)
    return result

print("Trending:", trending_days(likes, 1000))
