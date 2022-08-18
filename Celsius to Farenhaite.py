#TEMPIRATURE CONVERSION PROGRAM
#Enter 1. For Celsius to Fahrenheit
#Enter 2. For Fahrenheit to Celsius
#Enter 3 to Quit: 2
#Enter Fahrenheit Temperature: -15
#-15 Fahrenheit is equivalent to “-9.44” Celsius
#Enter 1. For Celsius to Fahrenheit
#Enter 2. For Fahrenheit to Celsius:
#Enter 3 to Quit: 1
#Enter Celsius Temperature: 53
#53 Celsius is equivalent to “127.4” Fahrenheit
#Course Title: IT5016: Software Development Fundamentals
#Enter 1. For Celsius to Fahrenheit
#Enter 2. For Fahrenheit to Celsius:
#Enter 3 to Quit: 3
#Note: Temperature below -271.15°C (absolute zero) does not exist on earth


Fahrenheit = int(raw_input("Enter a temperature in Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5.0/9.0

print "Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C"
Convert Celsius to Fahrenheit


#!/usr/bin/env python
Celsius = int(raw_input("Enter a temperature in Celsius: "))

Fahrenheit = 9.0/5.0 * Celsius + 32

print "Temperature:", Celsius, "Celsius = ", Fahrenheit, " F"
