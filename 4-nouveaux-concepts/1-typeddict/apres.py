from typing import NotRequired, TypedDict



# Pour créer un TypedDict, on va simplement créer une classe
# qui hérite de `TypedDict`. Quand on veut que l'ensemble des clés
# soient optionnelles, on peut rajouter juste après `TypeDict` : `total=False`.
class Article(TypedDict):
    
    # Chaque élément défini ci-dessous sera une clé avec 
    # le type de sa valeur. Chaque clé est une chaîne de 
    # caractères 
    nom: str 
    prix: float 
    taille: int 
    
    # Quand on veut qu'uniquement une clé soit optionnelle
    # on peut utiliser l'annotation de type générique `NotRequired`.
    reduction: NotRequired[float]
    
    # Il n'est pas possible de rajouter des méthodes dans un TypedDict
    # car ils sont uniquements utilisés pour donner des annotations complexes
    # à un dictionnaire. 
    
    
    
if __name__ == '__main__':
    article : Article = {
        "nom": "Chaussures",
        "prix": 55.5,
        "taille": 42,
        "reduction": 0.2
    }