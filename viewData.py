import sqlite3
conn = sqlite3.connect('deliveryData.db')
c = conn.cursor()


class ViewAverages:

    def view_avg_gross_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData')
        for row in c.fetchone():
            print('Your all time average tip is $', format(row, ".2f"))

    def view_avg_black_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData WHERE race = "BLACK"')
        for row in c.fetchone():
            print('The average BLACK person tips you $', format(row, ".2f"))

    def view_avg_white_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData WHERE race = "WHITE"')
        for row in c.fetchone():
            print('The average WHITE person tips you $', format(row, ".2f"))

    def view_avg_latino_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData WHERE race = "LATINO"')
        for row in c.fetchone():
            print('The average LATINO person tips you $', format(row, ".2f"))

    def view_avg_asian_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData WHERE race = "ASIAN"')
        for row in c.fetchone():
            print('The average ASIAN person tips you $', format(row, ".2f"))

    def view_avg_other_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData WHERE race = "OTHER"')
        for row in c.fetchone():
            print('The average OTHER race tips you $', row)

    def view_net_tip(self):
        c.execute('SELECT (SUM(grossTip) + SUM(delCharge)) - (SUM(miles)* SUM(gasWearCost)) FROM deliveryData')
        for row in c.fetchone():
            print(format(row, ".2f"))

