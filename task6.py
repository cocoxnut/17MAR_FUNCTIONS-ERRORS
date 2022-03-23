at = 10
in = 15
wo = 20

try:
	for e in range(-at, at):
		print(wo / e)'''
		if at > '5':
			print("at > 5)
except SyntaxError:
	print("Wrong syntax")
except: IndentationError:
	print("Wrong tab usage:)
except TypeError:
	print("STR cannot be divided to INT")
