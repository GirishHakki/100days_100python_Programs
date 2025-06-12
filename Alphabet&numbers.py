# Day 3

# write a program to check character is Alphabet, Digit or special character

ch = input("Please enter any character : ")

if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
    print("The entered character", ch ,"is alphabet")

elif (ch >= '0' or ch <= '9'):
    print("The entered character", ch, "is Digit")

else:
    print("The entered character", ch, "is Special Character")