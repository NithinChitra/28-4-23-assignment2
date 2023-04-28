print("Book Descriptions below")
print()
print("Book1: Introduction to Python Programming -> Rs.499.00")
print("Book2: Python Libraries Cookbook -> Rs.855.00")
print("Book3: Data Science in Python ->Rs.645.00")
print()
d={}
try:
    while(True):
        val=int(input("Enter which book you want(enter book no.): "))
        quantity=int(input("Enter quantity: "))
        d[val]=quantity
        a=int(input("Enter 0 to stop buying and 1 to continue buying: "))
        if a==0:
            break
except:
    print("Exception occured...")
    exit(0)
total_amount = (d[1]*499)+(d[2]*855)+(d[3]*645)
print()
print("Books amount is:",total_amount)
gst_amount = total_amount*0.12
print("GST costs:",gst_amount)
print("Delivery Charges: Rs.250.00",)
bill_amount = total_amount+gst_amount+250
print()
print("Bill amount->",bill_amount)


