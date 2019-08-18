MORSE_CODE = { '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','-----':'0'} 

def decodeMorse(morse_code):
	# ToDo: Accept dots, dashes and spaces, return human-readable message
	frase_completa = ""
	
	lista_palabras = morse_code.strip().split("   ")
	
	print("lista_palabras: ",lista_palabras)
	
	for palabra in lista_palabras:
		print("palabra: ", palabra)
		lista_letras = palabra.split(" ")
		print("lista_letras", lista_letras)
		
		for letra in lista_letras:
			print("letras :" , MORSE_CODE[letra])
			frase_completa = frase_completa+MORSE_CODE[letra]
		frase_completa = frase_completa+" " 
	return frase_completa.strip()


def test_and_print(got, expected):
	if got == expected: 	
		#test.expect(True)
		print("Test Exitoso")
	else:
		#print("<pre style='display:inline'>Got {}, expected {}</pre>".format(got, expected))
		#test.expect(False)
		print("Test no Exitoso :(")

#test.describe("Example from description")
test_and_print(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDEE')

#test.describe("Your own tests")
#decodeMorse('.... . -.--   .--- ..- -.. .')
# Add more tests here

