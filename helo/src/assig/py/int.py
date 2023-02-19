#3.    Write a program to find the simple interest (si=p*t*r/100)
def simple_interest(p, t, r):
    print("principle amount", p)
    print("time period", t)
    print("interest rate", r)
    si = (p * t * r)/100
    print("the simple interest amount", si)
simple_interest(10000,2,3)

