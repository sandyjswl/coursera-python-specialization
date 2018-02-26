hrs = float(input("Enter Hours:"))
rate=float(input("Enter Rate:"))
if hrs<=40:
    print(hrs*rate)
elif hrs>40:
    print(40*rate+(hrs-40)*(1.5*rate))
    
