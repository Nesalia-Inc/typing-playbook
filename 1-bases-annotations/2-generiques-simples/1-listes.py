# Les listes sont le premier type générique que l'on va voir. 
# Un type générique est un type qui est caractérisé par un autre type. 
# Par exemple, une liste d'entiers n'est pas la même chose qu'une liste
# de chaînes de caractères. La différence est causée par les éléments de 
# cette liste. 

# Quand on annotes une liste, on doit prendre en compte le type de ses éléments. 
# La syntaxe générale pour annoter une liste est `list[type_elements]`. Une liste 
# d'entiers aura donc l'annotation `list[int]`. 


def somme(nombres : list[int]) -> int:
    resultat = 0
    
    # On a défini que `nombres` est une liste d'entiers.
    # Le type checker comprends donc que chaque élément
    # de cette liste est un entier. Cela veut aussi dire
    # que si tu cherches à ajouter des éléments dans cette 
    # liste, tu ne pourras que ajouter des entiers.
    for nombre in nombres:
        resultat += nombre 
        
    return resultat



class Monstre:
    def __init__(self, vie : int, attaque : int) -> None:
        self.vie = vie 
        self.attaque = attaque 
        
        
    def mourir(self) -> None:
        self.vie = 0 
        
        

def supprimer(monstres : list[Monstre], attaque_requise : int) -> None:
    for monstre in monstres:
        if monstre.attaque < attaque_requise:
            monstre.mourir()
            


