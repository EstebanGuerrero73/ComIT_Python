# Develop a program to generate invoices to customers and purchase orders from suppliers.
# The system displays a menu asking if you want to make an invoice or purchase order
# In case of an invoice, it asks for the client’s data  and in case of being PO enter the supplier’s data.
# Then the program asks to enter up to 10 items (may be less) with description and its value

# At the end it calculates the net, GST, PST and finally shows on screen all the data of the invoice (or PO). 
# One thing per line:

# Invoice Number (PO)
# Customer number (Supplier)
# Customer name (Supplier)
# ————————
# Items with the value of each
# ———————- 
# Net
# GST
# PST
# Total

print("\n\n   * * * * *   INVOICES AND PURCHASE ORDERS GENERATOR  * * * * *   ")
print("\nTo generate an invoice to customers please enter: 1")
print("\nTo generate a purchase order from suppliers please enter: 2")

menu = input("\nPlease enter your choice: ")

print("\n   * * * * * * * * * * * * * * * * * * * * * * * * * *   ")

if menu == "1":
    name = input("\nPlease enter the name of the customer: ")
    phone = input("\nPlease enter the phone of the customer: ")
    invOrPo = input("\nPlease enter the number of the invoice: ")

if menu == "2":
    name = input("\nPlease enter the name of the supplier: ")
    phone = input("\nPlease enter the phone of the supplier: ")
    invOrPo = input("\nPlease enter the number of the purchase order: ")

item_number = int(input("\nPlease enter the number of items: "))

items = []
subtotal = 0
for i in range(item_number):
    item = input(f"\nPlease enter the item number {i+1}: ")
    value = input(f"\nPlease enter the value of the item number {i+1} ($): ")
    items.append([item, value])
    subtotal += float(value)

gst = subtotal * 0.05
pst = subtotal * 0.03
total = subtotal + gst + pst


print("\n   * * * * * * * * * * * * * * * * * * * * * * * * * *   ")

if menu == "1":
    print("\n\n   * * * * *                  INVOICE                  * * * * *   ")
    print("\n--------------------------------------------------------------------------")
    print(f"\nInvoice number: {invOrPo}")
    print(f"\nCustomer name: {name}")
    print(f"\nCustomer phone: {phone}")

if menu == "2":
    print("\n\n   * * * * *                PURCHASE ORDER                * * * * *   ")
    print("\n--------------------------------------------------------------------------")
    print(f"\nPurchase order number: {invOrPo}")
    print(f"\nSupplier name: {name}")
    print(f"\nSupplier phone: {phone}")

print("\n--------------------------------------------------------------------------")

print("\nITEM\t\t\tVALUE")

for i in items:
    print(f"\n{i[0]}\t\t\t{i[1]} $")

print("\n--------------------------------------------------------------------------")

print(f"\nSubtotal:\t\t{subtotal} $")
print(f"\nGST (5%):\t\t{gst} $")
print(f"\nPST (3%):\t\t{pst} $")
print("\n--------------------------------------------------------------------------")
print(f"\nTOTAL:\t\t\t{total} $")

print("\n--------------------------------------------------------------------------")

input("\n\n\nPlease press Enter to exit ...\n\n\n")


