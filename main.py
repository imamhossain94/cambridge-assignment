import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Task 1

HomeToStart = [["C1", 1.50], ["C2", 3.00], ["C3", 4.50], ["C4", 6.00], ["C5", 8.00]]
StartToEnd = [["M1", 5.75], ["M2", 12.50], ["M3", 22.25], ["M4", 34.50], ["M5", 45.00]]
EndToDest = [["F1", 1.50], ["F2", 3.00], ["F3", 4.50], ["F4", 6.00], ["F5", 8.00]]

PassengerAccounts = []
Bookings = []


def generate_unique_id(previous_id):
    return previous_id + 1


def create_account():
    print('\nCreate New Account')
    name = input("Enter your name: ")
    account_number = 1
    if PassengerAccounts:
        account_number = generate_unique_id(PassengerAccounts[len(PassengerAccounts) - 1][0])
    PassengerAccounts.append([account_number, name])
    print("Account Created!.\nYour account number is: %s\nYour name is: %s\n" % (account_number, name))


def pick_price_and_code(code_and_price_list):
    for item in code_and_price_list:
        print(item)
    code = input("Enter a code from the above list:")
    price = 0.0
    for item in code_and_price_list:
        if item[0] == code:
            price = item[1]
    if price == 0.0:
        print("Invalid code. Try again.")
        goto(1)
    return [code, price]


def new_bookings():
    print("Create New Bookings")
    passenger_account_number = int(input("Enter your account number: "))
    if passenger_account_number not in [item for sublist in PassengerAccounts for item in sublist]:
        print("Account number not exist!")
        goto(1)

    booking_number = 1
    if Bookings:
        booking_number = generate_unique_id(Bookings[len(Bookings) - 1][0])

    journey_start_time = int(input("Enter the journey start time in hour: "))

    print("Home to start list:")
    home_to_start = pick_price_and_code(HomeToStart)

    print("Start to end list:")
    start_to_end = pick_price_and_code(StartToEnd)

    print("End to destination list:")
    end_to_destination = pick_price_and_code(EndToDest)

    print("Trip Confirmation")
    print("The price for Home to Start is: ", home_to_start[1])
    print("The price for Start to End is: ", home_to_start[1])
    print("The price for End to Destination is: ", end_to_destination[1])
    total_price = home_to_start[1] + home_to_start[1] + end_to_destination[1]

    if journey_start_time > 10:
        print("Total trip price with 40% discount: ", round(total_price * 0.6, 2))
    else:
        print("Total trip price: ", total_price)

    confirm_booking = input("Confirm booking.(y/n): ")
    if confirm_booking in ('y', 'Y'):
        Bookings.append([
            booking_number,
            passenger_account_number,
            journey_start_time,
            home_to_start[0],
            home_to_start[1],
            start_to_end[0],
            start_to_end[1],
            end_to_destination[0],
            end_to_destination[1]
        ])
        print("Your trip is booked successfully")
    else:
        goto(1)


def print_details():
    for item in PassengerAccounts:
        print(item)

    for item in Bookings:
        print(item)


def goto(line_number):
    global line
    line = line_number


line = 1
if __name__ == '__main__':
    while True:
        if line == 1:
            print("Enter 1 for new account.")
            print("Enter 2 to make a new booking.")
            print("Enter 3 to view details.")
            print("Enter -1 to end the program.")
            choice = -1

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("\nPlease enter a valid choice:\n")
                goto(1)
                continue

            if choice == 1:
                create_account()
            elif choice == 2:
                new_bookings()
            elif choice == 3:
                print_details()
            elif choice == -1:
                print("\nProgram closed!\n")
                break
            else:
                print("\nPlease enter a valid choice:\n")
            goto(1)
