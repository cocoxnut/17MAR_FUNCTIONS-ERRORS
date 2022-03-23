try:
	lst = []
	for i in renge(10):
		lst.apend(i)

		a = list(revesed(lst))
		sls_obj = slice('0','8')
		print(а[sls_obj])
except SyntaxError:
	print("Syntax is not correct")
except IndentationError:
	print("Tab is used incorrectly")
except NameError:
	print("Name is incorrect")

