name = input("Enter the Customer name : ")
cost = float(input("Enter the cost of the product : "))
qty = float(input("Enter the quantity of the product : "))
amount = cost * qty
gst = 12 * cost / 100
total = amount + gst

if total < 1000:
    discount  = 0
elif total < 3000:
    discount = 0.1 * total
else:
    discount = 0.2 * total

print("Amount is ",amount)
print("GST is ",gst)
print("Discount is ",discount)
print("Amount to be paid ",total-discount)