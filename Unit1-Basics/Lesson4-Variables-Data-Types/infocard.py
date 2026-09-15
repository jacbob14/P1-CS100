"""
Lesson 4 Activity: Student Info Card
CS100: Roadmap to Computing

Build the card shown at the bottom of this file, using your own details.

Everything you need is from today: variables, the four data types,
calculations, type(), and f-strings.

Work top to bottom. Run after every step.
Save before you run. Commit and push when your output matches.
"""

WIDTH = 40


# --- Step 1: your information -----------------------------------
# Fill these in with YOUR details. Keep the types as marked:
# a name is a str, an age is an int, a GPA is a float, and
# honor-student is a bool (True or False, capitalized, no quotes).

my_name = "Jacob"                  # str
my_age = 15                    # int
my_gpa = 3.96                  # float
is_honor_student = True      # bool
my_grade = 10                 # int
favorite_subject = "Computer Science"         # str


# --- Step 2: calculations ---------------------------------------
# Each of these should make a NEW value out of the ones above.
# Do not type the answers in - let Python work them out.

# TODO: age_in_5_years
age_in_5_years = my_age + 5

# TODO: years_until_graduation   (grade 12 minus your grade)
years_until_graduation = 12 - my_grade

# TODO: age_at_graduation        (use the variable you just made)
age_at_graduation = my_age + years_until_graduation

# --- Step 3: the card -------------------------------------------
# Borders are WIDTH wide. The title is centered - calculate the
# padding from WIDTH and len(title), don't count spaces.
# Use f-strings for every line that shows a variable.
print("=" * WIDTH)
print(f"Name: {my_name} ")
print(f"Grade: {my_grade}")
print(f"GPA: {my_gpa}")
print(f"Favorite subject: {favorite_subject}")
print(f"Honor student: {is_honor_student}")
print("-" * WIDTH)
print(f"Age in 5 years: {age_in_5_years}")
print(f"Years until graduation: {years_until_graduation}")
print(f"Age at graduation: {age_at_graduation} ")
print("=" * 40)


# --- Step 4: show the types -------------------------------------
# Print the type of four of your variables, plus ONE of your
# calculated values. Use type().
# Look closely at what the calculated one comes out as.
print(" ")
print("TYPES USED")
print(my_name + f"         -> {type(my_name)}")
print(str(my_age) + f"         -> {type(my_age)}")
print(str(my_gpa) + f"         -> {type(my_gpa)}")
print(str(is_honor_student) + f"         -> {type(is_honor_student)}")
print(str(age_in_5_years) + f"         -> {type(age_in_5_years)}")

# =============================================================
# TARGET OUTPUT  (yours will show your own details)
# =============================================================
# ========================================
#            STUDENT INFO CARD
# ========================================
# Name: Jordan Rivera
# Age: 16
# Grade: 10
# GPA: 3.75
# Favorite subject: Computer Science
# Honor student: True
# ----------------------------------------
# Age in 5 years: 21
# Years until graduation: 2
# Age at graduation: 18
# ========================================
#
# TYPES USED
# my_name           -> <class 'str'>
# my_age            -> <class 'int'>
# my_gpa            -> <class 'float'>
# is_honor_student  -> <class 'bool'>
# age_in_5_years    -> <class 'int'>


# =============================================================
# STRETCH (optional)
# =============================================================
# Change my_grade to a different year. The card should still work
# and every calculation should update on its own. If you have to
# edit a number anywhere else, you typed an answer instead of
# calculating it.