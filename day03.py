# calculating student percentage

name = input("Enter name : ")
Kannada = float(input("Enter marks in Kannada : "))
eng = float(input("Enter marks in eng : "))
math = float(input("Enter marks in math : "))
sci = float(input("Enter marks in sci : "))
sst = float(input("Enter marks in sst : "))

total = Kannada + eng + math + sci + sst
per = total/5
print("-------------------")
print("Report card for ",name)
print("-------------------")
print("Total Marks Scored ",total)
print("Percentage Marks ",per,"%")
if per >=40:
    print("   Congratulations !!!")
else:
    print("   Sorry, Try Again")
print("-------------------")