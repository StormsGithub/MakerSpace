# Python Workshop, Activity 08 (Extended)
def CelsiusToFahrenheit():
	temperature = float(input("What is the temperature?"))
	result = temperature * (9/5) + 32
	print(temperature, "c converted to", result, "f")

def FahrenheitToCelsius():
	temperature = float(input("What is the temperature?"))
	result = (temperature - 32) * (5/9)
	print(temperature, "f converted to", result, "c")

def KmhToMph():
	speed = float(input("What is the speed?"))
	result = speed / 1.609344
	print(speed,"Km/h converted to", result,"Mp/h")

def MphToKmh():
	speed = float(input("What is the speed?"))
	result = speed * 1.609344
	print(speed,"Mp/h converted to", result,"Km/h")

# Start infinite loop
while True:
	# Print a menu
	print("------------------")
	print("1 - Celsius to Fahrenheit")
	print("2 - Fahrenheit to Celsius")
	print("3 - Km/h to Mp/h")
	print("4 - Mp/h to Km/h")
	print("------------------")

	conversion = input()

	if conversion == "1":
		CelsiusToFahrenheit()
	elif conversion == "2":
		FahrenheitToCelsius()
	elif conversion == "3":
		KmhToMph()
	elif conversion == "4":
		MphToKmh()
