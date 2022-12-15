# Python Workshop, Activity 08

# Get user input
unit = input("Are you converting from Celsius or Fahrenheit? c/f")
temperature = float(input("What is the temperature?"))

def CelsiusToFahrenheit(celsius):
	result = celsius * (9/5) + 32
	print(temperature, "c converted to:", result, "f")

def FahrenheitToCelsius(fahrenheit):
	result = (fahrenheit - 32) * (5/9)
	print(temperature, "f converted to:", result, "c")


if unit == "c":
	CelsiusToFahrenheit(temperature)
elif unit == "f":
	FahrenheitToCelsius(temperature)
