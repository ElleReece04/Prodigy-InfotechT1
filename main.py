unit = input("Is this temperature in Celsius, Fahrenheit, or Kelvin (C/F/K): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    fahrenheit_temp = round((9 * temp) / 5 + 32, 1)
    kelvin_temp = round(temp + 273.15, 1)
    print(f"The temperature in Fahrenheit is: {fahrenheit_temp}°F")
    print(f"The temperature in Kelvin is: {kelvin_temp} K")
elif unit == "F":
    celsius_temp = round((temp - 32) * 5 / 9, 1)
    kelvin_temp = round((temp - 32) * 5 / 9 + 273.15, 1)
    print(f"The temperature in Celsius is: {celsius_temp}°C")
    print(f"The temperature in Kelvin is: {kelvin_temp} K")
elif unit == "K":
    celsius_temp = round(temp - 273.15, 1)
    fahrenheit_temp = round((temp - 273.15) * 9 / 5 + 32, 1)
    print(f"The temperature in Celsius is: {celsius_temp}°C")
    print(f"The temperature in Fahrenheit is: {fahrenheit_temp}°F")
else:
    print(f"{unit} is an invalid unit of measurement")
