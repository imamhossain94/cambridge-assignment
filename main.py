# Task 1

HomeToStart = [["C1", 1.50], ["C2", 3.00], ["C3", 4.50], ["C4", 6.00], ["C5", 8.00]]
StartToEnd = [["M1", 5.75], ["M2", 12.50], ["M3", 22.25], ["M4", 34.50], ["M5", 45.00]]
EndToDest = [["F1", 1.50], ["F2", 3.00], ["F3", 4.50], ["F4", 6.00], ["F5", 8.00]]

PassengerAccounts = []
Bookings = []


def generate_unique_id(previous_id):
    return previous_id + 1


def create_account():
    print('Create New Account')
    name = input("Enter your name: ")
    account_number = 1
    if PassengerAccounts:
        print(generate_unique_id(PassengerAccounts[len(PassengerAccounts) - 1][0]))
    PassengerAccounts.append([account_number, name])
    print(PassengerAccounts)


def new_bookings():
    print("Create New Bookings")



if __name__ == '__main__':
    create_account()
