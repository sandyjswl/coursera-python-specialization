largest = None
smallest = None
result=[]
while True:
    num = input("Enter a number: ")
    if num=='done': break
    try:
        num_int=int(num)
        result.append(num_int)
    except:
        print("Invalid input")
        
    

print("Maximum is "+str(max(result)))
print("Minimum is "+str(min(result)))