net = (1, 2, 3, 'girl', 'boy', 1, 2, 3, 'board', 'class')
print(set(net))

values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
conv_list = []
for i in list(values):
	try :
		if list(i) == i:
			conv_list.add(i)
			print(conv_list, True)
		else :
			print(False)
	except:
		print("Something went wrong")




    
