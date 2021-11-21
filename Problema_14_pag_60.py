#Elaboraţi un program care citeşte de la tastatură două şiruri de caractere şi afişează pe ecran:
#a) caracterele care se întâlnesc cel puţin în unul dintre şiruri;
#b) caracterele care apar în ambele şiruri;
#c) caracterele care apar în primul şi nu apar în şirul al doilea
a = set(input("Introdu sirul a de caractere: "))
b = set(input("introdu sirul b de caractere: "))
for i in a:
	print(i.split(), end=" ")

print("\n")
for z in b:
	print(z.split(), end=" ")

print("\nElementele ce se intalnesc cel putin in unul din sirui: ", a.union(b))
print("Elementele ce se intalnesc in ambele siruri: ", a.intersection(b))
print("Elementele ce nu se intalnesc in ambele siruri 1: ", a.difference(b), "\nElementele ce nu se intalnesc in ambele siruri 2: ", b.difference(a))