from dynamicDataEntry import DynamicDataEntry

myDelivery = DynamicDataEntry()


def main():
    valid_choices = ('1', '2', '0')
    print("\nDelivery Earnings Tracker")
    choice = input("Press 1 to Enter Delivery Data, Press 2 for Options, Press 0 to quit: ")
    while choice not in valid_choices:
        choice = input("INPUT ERROR! Press 1 to Enter Delivery Data, Press 2 for Options, Press 0 to quit: ")
    if choice == '1':
        myDelivery.get_gross_tip()
        myDelivery.get_miles()
        myDelivery.get_demographic()
        myDelivery.put_in_database()
    elif choice == '2':
        options_menu()
    elif choice == '0':
        quit()


def options_menu():
    valid_choices = ('1', '2', '3', '4', '5', '0')
    choice = input('1: View Data\n'
                   '2: Change Gas / Wear Rate\n'
                   '3: Change Delivery Charge\n'
                   '0: Go Home: ')
    while choice not in valid_choices:
        choice = input('ERROR! Try again\n'
                       '1: View Data\n'
                       '2: Change Gas / Wear Rate\n'
                       '3: Change Delivery Charge\n'
                       '0: Go Home: ')
    if choice == '1':
        myDelivery.display_data()
    elif choice == '2':
        myDelivery.change_gas_wear_rate()
        options_menu()
    elif choice == '3':
        myDelivery.change_delivery_charge()
        options_menu()
    elif choice == '0':
        main()


while True:
    main()

