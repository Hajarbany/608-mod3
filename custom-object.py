# python object representing a purchase for a given amount
class purchase(object):
    def __init__(self, amount):
        self.amount = amount
        
    def calculatetax(self, taxpercent):
        return self.amount * taxpercent/100.0
        
    def calculatetip(self, tippercent):
        return self.amount * tippercent/100.0
        
    def calculatetotal(self, taxpercent, tippercent):
        return self.amount * (1 + taxpercent/100.0 + tippercent/100.0)
        
# create purchase object given an amount
purchase = purchase(100.0)

# set the tax and tip percentages
taxpercent = 7.5
tippercent = 20.0

# use the object to calculate tax and tip
tax = purchase.calculatetax(taxpercent)
tip = purchase.calculatetip(tippercent)

# display some useful information
print ('tax: ',tax)
print ('tip: ', tip)
print ('total:', purchase.calculatetotal(taxpercent, tippercent))

#Hajar Banyalmarjeh
