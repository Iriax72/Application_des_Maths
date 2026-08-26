# 0.1) ================
print(4.2/2)
# 2.1

# 0.2) ================
a = 23
b = 'hello'
c = 2
print(a + 5)
print(a + 1)
a = a + c
print(a)
c = c + a
print(c)
print(b + a)
"""
28
22
25
25
hello23
"""

# 0.3) ================
print("L'intelligence est la capacité de résoudre des problèmes nouveaux."[2:])
print("L'intelligence est la capacité de résoudre des problèmes nouveaux."[-2:])
print("L'intelligence est la capacité de résoudre des problèmes nouveaux."[::-2])
# 'intelligence est la capacité de résoudre des problèmes nouveaux.'
# 'x.'
# 'Litliec s acpct d rsuredspolmsnueu.'

# 0.4) ================
for k in range(3):
    k = k + 2
    print(k)
"""
2
3
4
"""

for k in range(6):
    if k%2 == 1:
        print(k)
"""
1
3
5
"""

for k in range(2, 8, 2):
    print(k)
"""
2
4
6
"""

# 0.5) ================
a = 0
while n < 17:
    print(n)
    n = n + 2
"""
0
2
4
6
8
10
12
14
16
"""

n = 1
while n**2 + 3*n < 15:
    print(n)
    n += 1
"""
1
2
"""

# 0.6) ===================
"""
Le deuxieme bloc de code fait la même chose que le premier, le deuxieme return n'est jamais éxecuté puisque le premier interomp la fonction
Le troisième bloc de code ne retourne rien, on ne peut donc pas utiliser fonction() + n par exemple mais il affiche directement les données dans la console
"""

# 0.7) ====================
x=5
def f1(x):
    return x**2
print(f1(x),x)
"""
25
5
"""

# Je réinitialise les variables
del x

a = 5
def f2(x):
    return a+x
print(f2(x), a)
"""
Error: 'x' is not definded
"""

# Je réinitialise les variables
del a

a = 5
def f3(x):
    a = 2
    return a + x
print(f3(x), a)
"""
Error: 'x' is not definded
"""


# Je réinitialise les variables
del a

a = 5
def f4(x):
    a += 1
    return a + x
print(f4(x), a)
"""
Error: 'x' is not definded
"""

# Je réinitialise les varaibles
del a

a = 5
def f5(x):
    global a 
    a += 1
    return a + x
print(f5(x), a)
"""
Error: 'x' is not definded
"""

# Je réinitialise les variabkes
del a

a = 5
def f6(x):
    global a
    a = 2
    return a + x
print(f6(x), a)
"""
Error: 'x' is not definded
"""

# 0.8) ==================
for n in range(10**6):
    if n * (n + 1) * (n + 2) >= 10**6:
        print(n)
        break

# 0.9) ==================
for n in range(2026):
    if n**2 > 2026:
        print(2)
        break

# 0.10) ====================
# a)
liste = []
for i in range(50):
    liste.append((i + 1) ** 2)
print(liste)

# b)
for carre in liste:
    if carre >= 2026:
        print(carre ** 0.5)
        break

# 0.11) =======================
def occurence(chiffre, nombre):
    occ = 0
    chiffre = string(chiffre)
    nombre = string(nombre)
    for c in nombre:
        if chiffre == c:
            occ += 1
    return occ

# tests
print(occurence(7, 778))
print(occurence(8, 20681))
print(occurence(5, 2771))
"""
Résultats attendus:
2
1
0
"""

# 0.12) ==================
x = int(input('Entrez un nombre'))
def factorielle(x):
    fac = 1
    for i in range(1, x+1):
        fac *= i
    print(fac)

# 0.13) ==================
for i in range(40):
    print('Informatique')

# 0.14) ===================
def somme(n):
    ret = 0
    for i in range(1, n+1):
        ret += i
    return 
    
def autreSomme(n):
    return (n + 1) * n/2

def encoreUne(n):
    return sum(range(1, n+1))