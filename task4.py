credit = float(input("Enter desired amount of credit: "))
rate = 3.47
if credit >= 50000:
	payable = (credit * rate) / 100
	print(round(payable, 2))
else:
	print("Goodbye")

