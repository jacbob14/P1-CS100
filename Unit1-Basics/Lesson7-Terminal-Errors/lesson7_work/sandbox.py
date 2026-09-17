"""
Lesson 7 SANDBOX
CS100: Roadmap to Computing
"""


# =============================================================
# QUICK TRY 1 - find your way around
# =============================================================
# Do these in the TERMINAL, not in this file.
# Open it with Ctrl + `  (backtick, top-left under Escape)
#
# 1. pwd          where am I right now?
# 2. ls           what is in this folder?
# 3. cd ..        go up one level
# 4. pwd          confirm you moved
# 5. cd cs100     come back down (use Tab to autocomplete)
# 6. clear        tidy the screen
#
# Write what pwd printed the first time:
# /Users/jbobrov/Desktop/Coding/BT-COMPSCI/P1-CS100


# =============================================================
# QUICK TRY 2 - build a workspace
# =============================================================
# Back in the terminal, in this folder:
#
#   mkdir lesson7_work            create a folder
#   cd lesson7_work               go into it
#   touch notes.txt               create an empty file
#   ls                            notes.txt should be there
#   cd ..                         back up one level
#   cp lesson7_sandbox.py lesson7_work/
#                                 copy this file INTO the folder
#                                 (trailing slash matters!)
#   cd lesson7_work
#   ls                            both files should be here
#   rm notes.txt                  delete the empty file
#   ls                            notes.txt is gone
#   cd ..                         back to where you started
#
# Write what ls showed after the cp:
# 
#
# Write what ls showed after the rm:
#   ______________________________________________


# =============================================================
# QUICK TRY 3 - run this file from the terminal
# =============================================================

print("It ran from the terminal!")

# In the terminal:   python lesson7_sandbox.py
#
# Now deliberately break it:
#   1. cd lesson7_work            go into the workspace
#   2. ls                         what is in here?
#   3. python lesson7_sandbox.py  run the WRONG copy from here
#      (you are running the copy that is inside lesson7_work,
#       but the file you want may not be here yet - check with ls)
#   4. Read the error. Write the last line here:
#        ____________________________________________
#   5. cd .. and run it again from the correct folder