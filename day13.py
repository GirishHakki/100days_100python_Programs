# factors of a number

num = int(input("Enter a number : "))

for a in range(1, num+1):
    if num % a == 0:
        print(a)