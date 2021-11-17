# Elaboraţi un program care afişează pe ecran toate submulţimile mulţimii {1, 2, 3, 4}.
import itertools
 
def findsubsets(a, z):
    return set(itertools.combinations(a, z))


def findsubsets(a, c):
    return set(itertools.combinations(a, c))

def findsubsets(a, d):
    return set(itertools.combinations(a, d))


def findsubsets(a, e):
    return set(itertools.combinations(a, e))

# Driver Code
a = {"A", "B", "C", "D"}
z=1
c = 2
d=3
e=4

print("submultimi cu 1 element: ", findsubsets(a, z))
print("submultimi cu 2 elemente: ",findsubsets(a, c))
print("submultimi cu 3 elemente: ",findsubsets(a, d))
print("submultimi cu 4 elemente: ",findsubsets(a, 4))