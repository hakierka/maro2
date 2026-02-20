def fahrenheit_to_celsius(t):
    t_celsius = (t - 32) * 5/9
    return t_celsius


def celsius_to_fahrenheit(t):
    t_fahrenheit = t * 9/5 + 32
    return t_fahrenheit


def kelvin_to_celsius(t):
    t_celsius = t + 273.15
    return t_celsius


def celsius_to_kelvin(t):
    t_kelvin = t - 237.15
    return t_kelvin

def fahrenheit_to_kelvin(t):
    t_kelvin = (t+459)* 5/9
    return t_kelvin


def Kelvin_to_fahrenheit(t):
    t_fahrenheit = (t + 459) * 5/9
    return t_fahrenheit

answer = input('Enter a temperature in Fahrenheit: ')
t_fahrenheit = float(answer)
t = fahrenheit_to_celsius(t_fahrenheit)
print("celsius: ", t)


answer =input('Enter a temperature in celsius:')
t_celsius = float(answer)
t = celsius_to_fahrenheit(t_celsius)
print("fahrenheit:" , t)



answer = input('Enter a temperature in celsius:')
t_kelvin = float(answer)
t = kelvin_to_celsius(t_kelvin)
print("celsius:", t)


answer = input('Enter a temperature in kelvin:')
t_celsius = float(answer)
t = celsius_to_kelvin(t_celsius)
print("kelvin", t)


answer = input ('Enter a temperature in fahrenhite:')
t_fahrenheit = float(answer)
t = fahrenheit_to_kelvin (t_fahrenheit) 
print("kelvin",t)

answer = input ('Enter a temperature in kelvin:')
t_kelvin = float(answer)
t = Kelvin_to_fahrenheit(t_kelvin)
print ("fahrenhite",t)



# I made a change!
# This is another change. By Pup