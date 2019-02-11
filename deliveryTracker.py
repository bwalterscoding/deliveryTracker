import sqlite3
import datetime

conn = sqlite3.connect('pizzaData.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS pizzaData(grossTip REAL, totalTip REAL, netTip REAL, miles REAL, date REAL, race TEXT)')


def dynamic_data_entry():


    gas_wear_tear = .18
    date = datetime.datetime.now()
    timestamp = date.strftime("%Y-%m-%d %H:%M ")
    order_price = float(input("Order Price: "))
    amt_given = float(input("Amount Given: "))
    grossTip = amt_given - order_price
    print("Gross Tip: ", format(grossTip, ".2f"))
    totalTip = grossTip + 1.25
    print("Tip with Delivery: ",format(totalTip,".2f"))
    print("Time Delivered: ",timestamp)
    miles = float(input("Round Trip Miles: "))
    netTip = totalTip - (miles * gas_wear_tear)
    print("Your net tip: ", format(netTip, ".2f"))
    race = input('Enter Race[white,black,latino,asian,other]: ')
    race = race.upper()

    c.execute("INSERT INTO pizzaData (grossTip, totalTip, netTip, miles, date, race) VALUES (?,?,?,?,?,?)",
              (format(grossTip,".2f"), format(totalTip,".2f"), format(netTip,".2f"), miles, timestamp, race))
    conn.commit()
    print()
    run_again = input("Run again? y or n: ")
    if run_again == "y":
        dynamic_data_entry()
    elif run_again == "n":
        main()

def status_check():
    choice = input("Press 1 for Total Tips, \nPress 2 for Net Tips, \nPress 3 for total Miles, \nPress 4 for average grossTip,\nPress 5 for highest tip,\nPress 0 for Home: ")
    if choice == "1":
        show_total_tips()
    elif choice == "2":
        show_net_tips()
    elif choice == "3":
        show_miles()
    elif choice == "4":
        show_avg_grossTips()
    elif choice == "5":
        show_hi_tip()
    elif choice == "0":
        main()
    else:
        print("Please, only 1,2, or 3")
        status_check()

def show_total_tips():
    c.execute('SELECT SUM(totalTip) FROM pizzaData')
    for row in c.fetchall():
        print(row)
        status_check()

def show_net_tips():
    c.execute('SELECT SUM(netTip) FROM pizzaData')
    for row in c.fetchall():
        print(row)
        status_check()

def show_miles():
    c.execute('SELECT SUM(miles) FROM pizzaData')
    for row in c.fetchall():
        print(row)
        status_check()

def show_avg_grossTips():
    c.execute('SELECT AVG(grossTip) FROM pizzaData')
    for row in c.fetchall():
        print(row)
        status_check()


def show_hi_tip():
    c.execute('SELECT MAX(grossTip) FROM pizzaData')
    for row in c.fetchall():
        print(row)
        status_check()






def main():
    print("Welcome to TIP TRACKER")
    print()
    select = input("Press 1 for data entry, Press 2 for Status check, Q to quit: ")
    select = select.upper()
    if select == "1":
        dynamic_data_entry()
    elif select == "2":
        status_check()
    elif select == 'Q':
        quit()
    else:
        print("Sorry, please enter a 1 or a 2")
    main()


create_table()
if __name__ == '__main__':
   main()
c.close()
conn.close()











    


    
  
   
