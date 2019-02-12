import sqlite3
conn = sqlite3.connect('deliveryData.db')
c = conn.cursor()


class ViewAverages:

    def view_avg_gross_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData')
        for row in c.fetchall():
            print('Your all time average tip is $', row)

    def view_avg_black_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData WHERE race = "BLACK"')
        for row in c.fetchall():
            print('The average black person tips you $', row)

    def view_avg_white_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData WHERE race = "WHITE"')
        for row in c.fetchall():
            print('The average white person tips you $', row)

    def view_avg_latino_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData WHERE race = "LATINO"')
        for row in c.fetchall():
            print('The average latino person tips you $', row)

    def view_avg_asian_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData WHERE race = "ASIAN"')
        for row in c.fetchall():
            print('The average asian person tips you $', row)

    def view_avg_other_tip(self):
        c.execute('SELECT AVG(grossTip) FROM deliveryData WHERE race = "OTHER"')
        for row in c.fetchall():
            print('The average unknown race tips you $', row)

    def view_net_tip(self):
        c.execute('SELECT (SUM(grossTip) + SUM(delCharge)) - (SUM(miles)* SUM(gasWearCost)) FROM deliveryData')
        for row in c.fetchall():
            print(row)

