
class Bike (object):
    def __init__(self, price, max_speed, miles):
        print "Initializing"
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "{} {} {}".format(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        self.miles += 10
        print self.miles
        return(self)

    def reverse(self):
        if self.miles > 5:
            self.miles-=5
        print self.miles
        return(self)


bike1 = Bike(200,"25pmh", 10)



bike1.ride().reverse().reverse().displayinfo()
