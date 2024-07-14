
#  write a prosren that will generate password for users- PyPassword Generator. Ask user how many letters, numbers and symbols

letters= ['a','b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

import random

ltr = int(input("how many letters would you like in your password: "))
num = int(input("how many numbers would you like in your password: "))
sym = int(input("how many symbols would you like in your password: "))

letter = random.sample(letters,ltr)
# print(letter)
number = random.sample(numbers,num)
# print(number)
symbol = random.sample(symbols,sym)
# print(symbol)

letter.extend(number)
letter.extend(symbol)
# # print(letter)
password = [l.replace("'", '') for l in letter]
random.shuffle(password)
finalPassword = ''.join(password)
print(finalPassword)