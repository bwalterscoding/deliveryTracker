from dynamicDataEntry import DynamicDataEntry
from viewData import ViewAverages
from viewTotals import ViewTotals

myDelivery = DynamicDataEntry()
myData = ViewAverages()
myDataTotals = ViewTotals()


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
        print('ORDER ENTRY SUCCESS!')
        myDelivery.put_in_database()
    elif choice == '2':
        options_menu()
    elif choice == '0':
        quit()


def options_menu():
    valid_choices = ('1', '2', '3', '4', '5', '0')
    choice = input('\nOPTIONS\n'
                   '1: View Totals\n'
                   '2: View Averages\n'
                   '3: Change Gas / Wear Rate\n'
                   '4: Change Delivery Charge\n'
                   '0: Go Home: ')
    while choice not in valid_choices:
        choice = input('ERROR! Try again\n'
                       #'1: View NetTip Data\n'
                       '2: Change Gas / Wear Rate\n'
                       '3: Change Delivery Charge\n'
                       '0: Go Home: ')#
    if choice == '1':
        view_totals_menu()

    elif choice == '2':
        view_averages_menu()

    elif choice == '3':
        myDelivery.change_gas_wear_rate()
        options_menu()

    elif choice == '4':
        myDelivery.change_delivery_charge()

    elif choice == '0':
        main()


def view_totals_menu():
    valid_choices = ('1', '2', '3', '4', '0')
    choice = input('\nVIEW TOTALS\n'
                   'Enter the number for the option you wish to select\n'
                   '1: Total Gross Tips all time\n'
                   '2: Total Delivery Charge Money\n'
                   '3: Total Net after gas/wear w/delivery charge\n'
                   '4: Total Mileage\n'
                   '5: Total Deliveries Taken\n'
                   '0: Go Back\n'
                   '>')

    if choice == '1':
        myDataTotals.view_total_gross_tips()
        view_totals_menu()
    elif choice == '2':
        myDataTotals.view_delivery_charge_earned()
        view_totals_menu()
    elif choice == '3':
        myDataTotals.view_net_tip_w_deliveryCharge()
        view_totals_menu()
    elif choice == '4':
        myDataTotals.view_total_mileage()
        view_totals_menu()
    elif choice == '5':
        myDataTotals.view_total_runs_taken()


def view_averages_menu():
    valid_choices = ('1', '2', '3', '4', '5', '6', '0')
    choice = input('\nAVERAGES MENU\n'
                   'Please enter the number for the data you wish to view\n'
                   '1: Average All Gross Tip\n'
                   '2: Average Caucasian Tip\n'
                   '3: Average African-American Tip\n'
                   '4: Average Latino Tip\n'
                   '5: Average Asian Tip\n'
                   '6: Average Other Tip\n'
                   '0: Go Back\n'
                   '> ')
    while choice not in valid_choices:
        print("Input Error! Try Again")
        choice = input('\nAVERAGES MENU\n'
                       'Please enter the number for the data you wish to view\n'
                       '1: Average All Gross Tip\n'
                       '2: Average Caucasian Tip\n'
                       '3: Average African-American Tip\n'
                       '4: Average Latino Tip\n'
                       '5: Average Asian Tip\n'
                       '6: Average Other Tip\n'
                       '0: Go Back')
    if choice == '1':
        myData.view_avg_gross_tip()
        view_averages_menu()
    elif choice == '2':
        myData.view_avg_white_tip()
        view_averages_menu()
    elif choice == '3':
        myData.view_avg_black_tip()
        view_averages_menu()
    elif choice == '4':
        myData.view_avg_latino_tip()
        view_averages_menu()
    elif choice == '5':
        myData.view_avg_asian_tip()
        view_averages_menu()
    elif choice == '6':
        myData.view_avg_other_tip()
        view_averages_menu()
    elif choice == '0':
        options_menu()


while True:
    main()
