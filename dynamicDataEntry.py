import datetime
date = datetime.datetime.now()

import sqlite3
conn = sqlite3.connect('deliveryData.db')
c = conn.cursor()


class DynamicDataEntry:

    def __init__(self):
        self.gas_wear_per_mile = .15
        self.delivery_charge = 1.5
        self.gross_tip = 0
        self.miles = 0
        self.race = ''
        self.date_stamp = date.strftime("%m-%d-%Y  ")
        self.run_counted = 1

    def get_gross_tip(self):
        order_price = float(input('Enter order price: '))
        amount_given = float(input('Enter amount given: '))
        self.gross_tip = amount_given - order_price

    def get_miles(self):
        self.miles = float(input('Enter total amount of miles driven for this delivery: '))

    def change_gas_wear_rate(self):
        self.gas_wear_per_mile = float(input('Enter new rate for gas and wear (default = .15 per mile): '))

    def change_delivery_charge(self):
        self.delivery_charge = float(input('Enter new delivery charge (default = $1.50 per run): '))

    def get_demographic(self):
        valid_races = ('WHITE', 'BLACK', 'LATINO', 'ASIAN', 'OTHER')
        self.race = input('Enter race of customer\n'
                          'WHITE, BLACK, LATINO, ASIAN, OTHER: ')
        self.race = self.race.upper()
        while self.race not in valid_races:
            self.race = input('ERROR!\n'
                              'Enter race of customer\n'
                              'WHITE, BLACK, LATINO, ASIAN, OTHER: ')
            self.race = self.race.upper()


    def display_data(self):
        print('\nDATA\n'
              'Current Gas&Wear Rate: ', self.gas_wear_per_mile, '\n'
                'Current Delivery Charge: ', self.delivery_charge, '\n'
                    'Gross Tip: ', format(self.gross_tip), '\n'
                        'Miles: ', self.miles, '\n'
                            'Race: ', self.race, '\n'
                                'Date Delivered: ', self.date_stamp, '\n'
                                    'Run Counted: ', self.run_counted)

    def put_in_database(self):
        c.execute(
            'CREATE TABLE IF NOT EXISTS deliveryData(grossTip REAL, miles REAL, date REAL, race TEXT, delCharge REAL, gasWearCost REAL, runCounted REAL)'
        )

        c.execute("INSERT INTO deliveryData (grossTip, miles, date, race, delCharge, gasWearCost, runCounted) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (self.gross_tip, self.miles, self.date_stamp, self.race, self.delivery_charge, self.gas_wear_per_mile, self.run_counted))
        conn.commit()


