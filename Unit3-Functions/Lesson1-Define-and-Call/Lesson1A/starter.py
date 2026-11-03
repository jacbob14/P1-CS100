"""Unit 3 Lesson 1A Activity - Profile Card
CS100: Roadmap to Computing

Build a profile card out of small functions that each do ONE job.

Expected output:

    ================
    @nasa
    Engagement: 750
    ================
    ================
    @tswift
    Engagement: 2750
    ================

Rubric:
    1. Four functions: line, print_handle, print_engagement, profile_card
    2. Every function starts with a one-line docstring
    3. profile_card CALLS the other three - it doesn't print anything itself
    4. Two calls to profile_card at the bottom, arguments in the right order
"""


# TODO 1: line() - prints a row of 16 = signs    
def line():
    """Prints a row of 16 = signs."""
    print("=" * 16)


# TODO 2: print_handle(username) - prints the username with @ in front
#         print_handle("nasa")  ->  @nasa
def print_handle(username):
    """Prints the username with @ in front."""
    print(f"@{username}")


# TODO 3: print_engagement(likes, shares, comments)
#         prints "Engagement: " and the three added together
#         print_engagement(500, 50, 200)  ->  Engagement: 750
def print_engagement(likes, shares, comments):
    """Prints Engagement: followed by the sum of likes, shares, and comments."""
    print(f"Engagement: {likes + shares + comments}")


# TODO 4: profile_card(username, likes, shares, comments)
#         calls line, print_handle, print_engagement, then line again
def profile_card(username, likes, shares, comments):
    """Prints a profile card by calling line, print_handle, and print_engagement."""
    line()
    print_handle(username)
    print_engagement(likes, shares, comments)
    line()


# TODO 5: call profile_card for both accounts
#         nasa:   500 likes, 50 shares, 200 comments
#         tswift: 2000 likes, 300 shares, 450 comments
profile_card("nasa", 500, 50, 200)
profile_card("tswift", 2000, 300, 450)
