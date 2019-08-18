def printer_error(s):
	denominador = len(s)
	numerador = 0
	for box_color in s:
		if ord(box_color) not in range(97,109+1):
			numerador += 1
	return "%s/%s" %(numerador,denominador)

print(printer_error("aaaaaaamxxx"))

#z = “In the basket are %s and %s” % (x,y)
			