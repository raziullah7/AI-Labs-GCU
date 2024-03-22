def calculate_ticket_price(age, day_of_week, is_holiday):
    full_price = 12.0
    discount_price = 8.0
    weekend_multiplier = 1.2
    holiday_multiplier = 1.5

    if age >= 18:
        ticket_price = full_price
    elif age < 12 or age >= 65:
        ticket_price = discount_price
    else:
        print("Invalid age.")
        return None

    if day_of_week in ["Saturday", "Sunday"]:
        ticket_price *= weekend_multiplier
    elif is_holiday:
        ticket_price *= holiday_multiplier

    return ticket_price


# main function
while True:
    age = int(input("Enter your age: "))
    day_of_week = input("Enter the day of the week: ").capitalize()
    is_holiday = input("Is it a holiday? (yes/no): ").lower() == "yes"

    ticket_price = calculate_ticket_price(age, day_of_week, is_holiday)

    if ticket_price is not None:
        print("The ticket price is:", "${:.2f}".format(ticket_price))
        
    another_ticket = input("Do you want to calculate another ticket price? (yes/no): ").lower()
    if another_ticket != "yes":
        break
