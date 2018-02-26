def computepay(h,r):
    if h<=40:
        return h*r
    elif h>40:
        return 40*r+(h-40)*(1.5*r)

hrs = float(input("Enter Hours:"))
rate=float(input("Enter rate:"))
p = computepay(hrs,rate)
print(p)