def due_amount(total_bill, paid_amount):
    return total_bill - paid_amount

bill = float(input("Enter total bill amount: "))
paid = float(input("Enter paid amount: "))

print("Customer due amount =", due_amount(bill, paid))