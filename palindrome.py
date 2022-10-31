print("Палиндром")
x = input('Please insert a word:')
y = ''.join(reversed(x))  # создает список связывает
z = x[::-1]  # строка
print(z)
pali = lambda p: x == p[::-1]
if x == y and x == z and pali(x):
    print('Is a palindrome')
    print("z", z)
    print("y", y)
    print("p", pali(x))
else:
    print('Is not a palindrome')