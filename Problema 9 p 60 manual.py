#Scrieţi un program care citeşte de la tastatură elementele mulţimilor A şi B şi afişează pe ecran:
#a) intersecţia mulţimilor A şi B;
#b) reuniunea mulţimilor A şi B;
#c) diferenţa mulţimilor A şi B;
#Mulţimile A şi B sunt formate din literele mari ale alfabetului latin.
a = set(eval(input("Introdu literele multimii a: ")))
b =  set (eval(input("introdu literele multimii b: " )))
c=set() #literele mari din multimea a
d=set() #literele mici din multimea b

for i in a: 
    if i==str(i):
        c.update(i.title())

for z in b:
    if z==str(z):
        d.update(z.title())

print(c)
print(d)
print("reuniunea literelor mari ale multimilor a si b: ", c.union(d))
print("Intersectia multimilor literelor mari ", c.intersection(d))
print('Diferenta1 dintre multimi ', c.difference(d), "\n", 'Diferenta2 dintre multimi ', d.difference(c))