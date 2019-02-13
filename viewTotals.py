import sqlite3
conn = sqlite3.connect('deliveryData.db')
c = conn.cursor()


class ViewTotals:

    def view_total_gross_tips(self):
        c.execute('SELECT SUM(grossTip) FROM deliveryData')
        for row in c.fetchone():
            print('Your all time total tips  $', row)

    def view_delivery_charge_earned(self):
        c.execute('SELECT SUM(delCharge) FROM deliveryData')
        for row in c.fetchone():
            print('Your all time total for delivery charges paid to you:  $ ', row)

    def view_net_tip_w_deliveryCharge(self):
        c.execute('SELECT (SUM(grossTip) + SUM(delCharge)) - (SUM(miles) * gasWearCost) FROM deliveryData')
        for row in c.fetchone():
            print('Your Total Accumulated Net Tips (w/ delivery charge w/ gas cost and wear included) $', row)

    def view_total_mileage(self):
        c.execute('SELECT SUM(miles) FROM deliveryData')
        for row in c.fetchone():
            print('You have driven', row, 'miles since you started')

    def view_total_runs_taken(self):
        c.execute('SELECT SUM(runCounted) FROM deliveryData')
        for row in c.fetchone():
            print('You have taken', format(row, ".0f"), 'deliveries')

