# This is a sample Python script.

from random import choice
from string import ascii_letters, digits

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# print(''.join(choice(ascii_letters) for i in range(50)))
# print(''.join(choice(digits) for i in range(12)))
lst = ''.join(choice(chars) for i in range(50))
print(lst)
print(sorted(lst))
print(''.join(sorted(lst)))

