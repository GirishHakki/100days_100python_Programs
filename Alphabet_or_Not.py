# Day 2

# write a program to identify if the character is an alphabet or not.

# Method 1 using (if else statement)

# ch = input("Please enter any character : ")
#
# if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
#     print("The entered character", ch ,"is alphabet")
#
# else:
#     print("The entered character", ch, "is not alphabet")

#    -----------------------------------------------------------------------


# Method 2 using "isalpha()"
# ---------------------

ch = input("Please enter any character : ")
if (ch.isalpha()):
    print("The entered character", ch, "is alphabet")
else:
    print("The entered character", ch, "is not alphabet")