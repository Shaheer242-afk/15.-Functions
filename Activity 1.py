def greet_customer ():
    print("Welcome to the lemonade stand!")
    print("Fresh Lemonade just for you!")

greet_customer ()

price_per_cup = float(input("Please enter price per cup: "))
cups_sold = int(input("Please enter cups sold: "))

def calculate_total(price, cups):
    total = price * cups
    return total


total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("Rounded cost: ", rounded_total)

amount_paid = float(input("Please enter total amount paid by the customer: "))

def calculate_chage(paid, total):
    change = paid - total
    return change

change_due = calculate_chage(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(cups):
    if cups <= 5:
        return "Wow, Big order thank you for your support!"
    else:
        return "Thanks for stopping by!"

closing_message = thank_you_message(cups_sold)


print("")
print("======LEMONADE STAND RECEIPT======")
print("Price Per Cup", price_per_cup)
print("Cups Sold", cups_sold)
print("Total Cost", total_cost)
print("Amount Paid", amount_paid)
print("Change Due", rounded_change)
print(closing_message)
print("==================================")