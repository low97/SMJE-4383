def celsius_to_fahrenheit(celsius_float):
	"""Convert celsius to fahrenheit"""
	return celsius_float * 1.8 +32

#main part of the program
print("convert celsius to fahrenheit.")
celsius_float = float(input("Enter temp in celsius: "))
#Call the conversion function
fahrenheit_float = celsius_to_fahrenheit(celsius_float)
#print output
print(celsius_float,"convert to ", fahrenheit_float, "Fahrenheit")
