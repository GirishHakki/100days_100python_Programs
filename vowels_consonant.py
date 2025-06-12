# Simplified Learner youtube channel
# Day 1

ch = input("Enter any Character: ")
print("-"*20)
if(ch == 'a' or ch == 'e' or ch =='i' or ch =='o' or ch =='u' or
     ch == 'A' or ch =='E' or ch =='I' or ch =='O' or ch =='U'):
    print(ch, "is a Vowel.")

elif ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
    print(ch, "is a consonant.")
else:
    print("Invalid Input! Please enter an Alphabet.")


















