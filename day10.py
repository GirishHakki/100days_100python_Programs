# profit or loss calculator

cp = float(input("Enter the cost price : "))
sp = float(input("Enter the selling price : "))
if sp > cp:
    print("Profit is Rs.",sp-cp)
elif cp > sp:
    print("Loss is Rs.",cp-sp)
else:
    print("No Profit No Loss")