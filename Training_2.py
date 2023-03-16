import json

class Flowerzzzzz:
    def __init__(self, color, name, typeOfPolen, numberPetals):
        self.color = color
        self.name = name
        self.typeOfPolen = typeOfPolen
        self.numberPetals = numberPetals
        
    def to_json(self):
        return json.dumps({
            'color': self.color,
            'name': self.name,
            'typeOfPolen': self.typeOfPolen,
            'numberPetals': self.numberPetals
        })
    
# Exemple d'utilisation
ma_jolie_fleur = Flowerzzzzz("Pink", "Pétulia des sables", "Polen de sable", 5)
print(ma_jolie_fleur.to_json())
