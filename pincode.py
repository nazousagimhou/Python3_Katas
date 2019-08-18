def validate_pin(pin):
    #return true or false
    lista_digitos = ['0','1','2','3','4','5','6','7','8','9']
    pin_length = len(pin)
    if pin_length == 4 or pin_length == 6:
    	print("tamaño correcto")
    	for caracter in pin:
    		if caracter not in lista_digitos:
    			print("caracter invalido:", caracter)
    			return False
    	print("PIN valido")
    	return True		
    else:
    	print("tamaño incorrecto :(")
    	return False

#validate_pin("24367H")
#validate_pin("")
#validate_pin("243678")
validate_pin("1234")