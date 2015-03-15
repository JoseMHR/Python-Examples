def computepay(h,r):
    if h > 40 :
    	sol = 40 * r + (h-40)*1.5*r
    else :
    	sol = h * r
    
    
    return sol

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")

h = float(hrs)
r = float(rate)

p = computepay(h,r)

print p
