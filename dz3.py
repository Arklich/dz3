word = (input("Введите слово: ")) 

a = word.count('a') 
e = word.count('e') 
i = word.count('i') 
o = word.count('o') 
u = word.count('u') 
y = word.count('y') 

q = word.count('q') 
w = word.count('w')
r = word.count('r')
t = word.count('t')
p = word.count('p')
s = word.count('s')
d = word.count('d')
f = word.count('f')
g = word.count('g')
h = word.count('h')
j = word.count('j')
k = word.count('k')
l = word.count('l')
z = word.count('z')
x = word.count('x')
c = word.count('c')
v = word.count('v')
b = word.count('b')
n = word.count('n')
m = word.count('m')

if a == 0: 
    print("a = False") 
if e == 0: 
    print("e = False") 
if i == 0: 
    print("i = False") 
if o == 0: 
    print("o = False") 
if u == 0: 
    print("u = False") 
if y == 0:  
    print("y = False") 
print(f"Гласных: {a + e + i + o + u}") 
print(f"Согласных: {a + e + i + o + u}")

count = 0
for i in word:
    if i == "a":
        count += 1
        print(f'Букв А в слове: {count}')

count1 = 0
for i in word:
    if i == "e":
        count1 += 1
        print(f'Букв E в слове: {count}')

count2 = 0
for i in word:
    if i == "y":
        count2 += 1
        print(f'Букв Y в слове: {count}')

count3 = 0
for i in word:
    if i == "U":
        count3 += 1
        print(f'Букв U в слове: {count}')

count4 = 0
for i in word:
    if i == "i":
        count4 += 1
        print(f'Букв I в слове: {count}')

count5 = 0
for i in word:
    if i == "o":
        count5 += 1
        print(f'Букв O в слове: {count}')