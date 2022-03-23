try:
	a = 45
	print(pay)
except NameError:
	print("No such name")

try:
	print(12 / "num")
except TypeError:
	print("STR cannot be divided to INT")

try:
	my_tuple = 1, 4, 7, 34, 89.6, "name"
	n = my_tuple[9]
	print(n)
except IndexError:
	print("No such index")
