# April 12, 2014
# Qualification Round
# "Cookie Clicker Alpha"
# = Kyra =

from time import time

#inpath = "B-sample.in"
inpath = "B-large.in"
#inpath = 'B-small-attempt0.in'
outpath = "B.out"

# Look if adding a fabric makes goal closer if we add gain to current rate
# for the price given
def OptForFabric(rate, gain, price, goal):
    current_time = (goal - price) / rate
    new_time = goal / (rate + gain)
    return new_time < current_time

# Just count time from 0 cookies to fabric price or to goal achieving
def TimeToNewOption(current_rate, price):
    return price / current_rate

# Main procedure
# Idea is: if we are to buy a fabric, we need to buy it just when we got
# enough cookies to do that, so we restart from 0 each time
def CookieTime(price, gain, goal):
    time = 0.0
    rate = 2
    while True:
        if not OptForFabric(rate, gain, price, goal):
            break
        time += TimeToNewOption(rate, price)
        rate += gain
    time += TimeToNewOption(rate, goal)
    return time
    
timestart = time()

fin = open(inpath, 'r')
fout = open(outpath, 'w')

T = int(fin.readline())
for case in range(1, T+1):
    C, F, X = map(float, fin.readline().split())
    cookietime = CookieTime(C, F, X)
    fout.write("Case #%d: %f\n" % (case, cookietime))
    #print "Case #%d: %f" % (case, cookietime)
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
