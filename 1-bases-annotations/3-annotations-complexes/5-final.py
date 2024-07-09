

from typing import Final


# Il est possible de créer des constantes en utilisant l'annotation
# de type générique `Final`. Elle prends en paramètre le type de la
# valeur de la constante. 
IDENTIFIANT : Final[int] = 123456789

# Une fois que la constante a été définie, on a une erreur qui est 
# renvoyée lorsqu'on essaye de la modifier. 
IDENTIFIANT = 1234 # Non...



def fonction(identifiant : int) -> None:
    identifiant = 1234 
    
    print(identifiant)
    
    
    
if __name__ == '__main__':
    fonction(IDENTIFIANT)
    
    


