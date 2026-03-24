#1. Create an Enum object and show a member name and value

#Write a Python program to create an Enum object and display a member name and value.

#Sample data :
#Member name: Albania
#Member value: 355

from enum import Enum
from enum import IntEnum

class country(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

print('\nMember name: {}'.format(country.Albania.name))
print('Member value: {}'.format(country.Albania.value))

# Iterate over an Enum class and display members and values

for data in country:
    print(data.name, data.value)

#3. Display Enum member names ordered by their values


print(('\n'.join(' ' + data.name for data in sorted(country))))
   
#4. Get All Values from an Enum Class

#Write a Python program to get all values from an enum class.

# method 1

list_of_values = []

for data in country:
    list_of_values.append(data.value)

print(list_of_values)

# method 2

country_code_list = list(map(int, country))

print(country_code_list)

#5. Get Unique Enumeration Values

# Write a Python program to get unique enumeration values.

class Countries(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    India = 355
    USA = 213

list_of_values2 = []

for data in Countries:
    if data.value not in list_of_values2:
        list_of_values2.append(data.value)
        print(data.name, data.value)




