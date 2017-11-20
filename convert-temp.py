# this script will convert celsius, fahrenheit, and kelvin to celsius, fahrenheit, or kelvin.

def fahrenheit_to_celsius(temp):
    converted = (temp - 32) * 5 / 9
    return converted

def fahrenheit_to_kelvin(temp):
    converted = ((temp * 9 / 5) + 32) + 274.15
    return converted

def celsius_to_fahrenheit(temp):
    converted = (temp * 9 / 5) + 32
    return converted

def celsius_to_kelvin(temp):
    converted = temp + 274.15
    return converted

def kelvin_to_celsius(temp):
    converted = temp - 274.15
    return converted

def kelvin_to_fahrenheit(temp):
    converted = ((temp - 274.15) * 9 / 5) + 32
    return converted

def main():
    temp = int(input('Enter the temperature you wish to convert: '))
    units = str(input('Is this C (celsius), F (Fahrenheit), or K (Kelvin)?'))
    units.lower()
    convert = str(input('Would you like this converted to C (celsius), F (Fahrenheit), or K (Kelvin)?'))
    convert.lower()
    if units == 'c' and convert == 'f':
        converted = celsius_to_fahrenheit(temp)
    elif units == 'c' and convert == 'k':
        converted = celsius_to_kelvin(temp)
    elif units == 'f' and convert == 'c':
        converted = fahrenheit_to_celsius(temp)
    elif units == 'f' and convert == 'k':
        converted = fahrenheit_to_kelvin(temp)
    elif units == 'k' and convert == 'f':
        converted = kelvin_to_fahrenheit(temp)
    elif units == 'k' and convert == 'c':
        converted = kelvin_to_celsius(temp)
    else:
        print('Invalid entry.')

    print('\n{} {} is equal to {} {}.\n'.format(temp, units.upper(), converted, convert.upper()))

main()

def test_c_to_k():
    assert celsius_to_kelvin(1) == 275.15

def test_c_to_f():
    assert celsius_to_fahrenheit(50) == 122

def test_k_to_c():
    assert kelvin_to_celsius(1) == -273.15

def test_k_to_f():
    assert kelvin_to_fahrenheit(77) == -321.07

def test_f_to_c():
    assert fahrenheit_to_celsius(98) == 36.7

def test_f_to_k():
    assert fahrenheit_to_kelvin(212) == 373.15
