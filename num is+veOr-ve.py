# Day 4

# Write a Program To Check Entered Number is Positive Or Negative

# method 2 using (if elif else statement)
# n = float(input("Enter any number: "))
# print("-"*20)
#
# if (n>0):
#     print(n, "is a Positive Number")
# elif (n==0):
#     print(n, "is Zero")
# else:
#     print(n, "is Negative Number")

#----------------------------------------------------------------------------

# method 2 using (nested if)

n = float(input("Enter any number : "))
print("-"*30)
if n >= 0:
    if n ==0:
        print(n, "is Zero")
    else:
        print(n, "is Positive Number")
else:
    print(n, "is Negative Number")
print("-"*30)











