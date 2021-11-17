#Scrieţi un program care citeşte de la tastatură elementele mulţimilor A şi B şi afişează pe ecran:
#a) intersecţia mulţimilor A şi B;
#b) reuniunea mulţimilor A şi B;
#c) diferenţa mulţimilor A şi B.
#Mulţimile A şi B sunt formate din numere întregi
a = set(eval(input("introdu elementele multimii a: ")))
b = set(eval(input("introdu elementele multimii b: ")))
print(a)
print(b)
d=1
for i in a :
    if type(i)!=type(1) :
        d=0

for  z in b:
    if type(z)!=type(1):
        d=0

if d==1:
    print("Uniunea multimilor a si b: ", a.union(b))
    print("Intersectia multimilor a si b", a.intersection(b))
    print("diferenta 1 a multimilor ", a.difference(b), "\n", "diferenta 2 ", b.difference(a))
else:
    print("eroare")
