def maximum(value1, value2, value3):
    """Return the maximum of three
values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
        
    return max_value

print('enter 3 numbers or strings to find the maximum')
value1 = input('enter value 1: ')
value2 = input('enter value 2: ')
value3 = input('enter value 3: ')

print('the maximum of your numbers is:', maximum(value1, value2, value3))

maximum(12,27,55)

           # Hajar Banyalmarjeh

def minimum(value1, value2, value3):
    """Return the minimum of three
values."""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
        
    return min_value

print('enter 3 numbers or strings to find the minimum')
value1 = input('enter value 1: ')
value2 = input('enter value 2: ')
value3 = input('enter value 3: ')

print('the minimum of your numbers is:', minimum(value1, value2, value3))

minimum(12,27,55)

