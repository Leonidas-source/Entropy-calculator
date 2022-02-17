import math
numbers = 0
lower = 0
upper = 0
a = (input("Введите свой пароль: "))
print(a)
b = len(a)
print(b)
if "1" in a:
    numbers = 10
if "2" in a:
    numbers = 10
if "3" in a:
    numbers = 10
if "4" in a:
    numbers = 10
if "5" in a:
    numbers = 10
if "6" in a:
    numbers = 10
if "7" in a:
    numbers = 10
if "8" in a:
    numbers = 10
if "9" in a:
    numbers = 10
if "0" in a:
    numbers = 10
if "a" in a:
    lower = 26
if "b" in a:
    lower = 26
if "c" in a:
    lower = 26
if "d" in a:
    lower = 26
if "e" in a:
    lower = 26
if "f" in a:
    lower = 26
if "g" in a:
    lower = 26
if "h" in a:
    lower = 26
if "i" in a:
    lower = 26
if "j" in a:
    lower = 26
if "k" in a:
    lower = 26
if "l" in a:
    lower = 26
if "m" in a:
    lower = 26
if "n" in a:
    lower = 26
if "o" in a:
    lower = 26
if "p" in a:
    lower = 26
if "q" in a:
    lower = 26
if "r" in a:
    lower = 26
if "s" in a:
    lower = 26
if "t" in a:
    lower = 26
if "u" in a:
    lower = 26
if "v" in a:
    lower = 26
if "w" in a:
    lower = 26
if "x" in a:
    lower = 26
if "y" in a:
    lower = 26
if "z" in a:
    lower = 26
if "A" in a:
    upper = 26
if "B" in a:
    upper = 26
if "C" in a:
    upper = 26
if "D" in a:
    upper = 26
if "E" in a:
    upper = 26
if "F" in a:
    upper = 26
if "G" in a:
    upper = 26
if "H" in a:
    upper = 26
if "I" in a:
    upper = 26
if "J" in a:
    upper = 26
if "K" in a:
    upper = 26
if "L" in a:
    upper = 26
if "M" in a:
    upper = 26
if "N" in a:
    upper = 26
if "O" in a:
    upper = 26
if "P" in a:
    upper = 26
if "Q" in a:
    upper = 26
if "R" in a:
    upper = 26
if "S" in a:
    upper = 26
if "T" in a:
    upper = 26
if "U" in a:
    upper = 26
if "V" in a:
    upper = 26
if "W" in a:
    upper = 26
if "X" in a:
    upper = 26
if "Y" in a:
    upper = 26
if "Z" in a:
    upper = 26
Number_of_Possible_Combinations = (numbers + lower + upper) ** b
print(Number_of_Possible_Combinations)
Entropy = math.log2(Number_of_Possible_Combinations)
print(str(Entropy) + " бит энтропии")
ENG = 2 ** (Entropy - 1)
print("Чтобы подобрать ваш пароль необходимо: ")
print(str(ENG) + " попыток")
