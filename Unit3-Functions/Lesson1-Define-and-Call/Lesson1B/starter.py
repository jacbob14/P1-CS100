"""Unit 3 Lesson 1B Activity - Streaming Settings
CS100: Roadmap to Computing

Write four functions that RETURN their answers. The tests at the bottom
are already written - don't change them. If you print inside a function
instead of returning, you'll see None appear in the output.

Expected output:

    Trending: False
    Trending: True
    premium 999
    student 10
    free 3
    guest 0
    1 Mbps 480p
    3 Mbps 720p
    5 Mbps 720p
    7 Mbps 1080p
"""


# TODO 1: calculate_engagement(likes, shares, comments)
#         returns the three added together
def calculate_engagement(likes, shares, comments):
    return likes + shares + comments


# TODO 2: is_trending(engagement)
#         returns True if engagement is over 1000, otherwise False
def is_trending(engagement):
    return engagement > 1000


# TODO 3: get_tier_perks(tier) - daily skips for a subscription tier
#         "premium" -> 999,  "student" -> 10,  "free" -> 3,  anything else -> 0
def get_tier_perks(tier):
    if tier == "premium":
        return 999
    elif tier == "student":
        return 10
    elif tier == "free":
        return 3
    else:
        return 0


# TODO 4: get_video_quality(mbps)
#         over 5 -> "1080p",  2 to 5 -> "720p",  under 2 -> "480p"
def get_video_quality(mbps):
    if mbps > 5:
        return "1080p"
    elif mbps >= 2:
        return "720p"
    else:
        return "480p"


# ---------- TESTS - don't change anything below this line ----------
print("Trending:", is_trending(calculate_engagement(500, 50, 200)))
print("Trending:", is_trending(calculate_engagement(2000, 300, 450)))
print("premium", get_tier_perks("premium"))
print("student", get_tier_perks("student"))
print("free", get_tier_perks("free"))
print("guest", get_tier_perks("guest"))
for mbps in range(1, 8, 2):
    print(mbps, "Mbps", get_video_quality(mbps))
