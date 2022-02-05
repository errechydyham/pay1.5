hours = input("Enter hours: ")
rate = input("Enter rate: ")
pay = 0 

if float(hours) <= 40: 
    pay = float(hours) * float(rate)
else: 
    pay = float(hours) * (float(rate) * 1.5) 

print("Your pay is: ", pay)