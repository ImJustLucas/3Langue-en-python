import random

# Definition de la classe 
class Citation:
    def __init__(self):
        self.citations = [
          "Qui avale une noix de coco, fait confiance a son anus.",
          "Attend d'avoir traversé la rivière pour dire que le crocodile a une sale gueule.",
          "On ne marche pas deux fois sur les testicules d'un aveugle.",
          "Quelque sois la taille d'un elephant, ses couilles remplissent une marmite"
          "- T'as les crampté ? - hein ? - Apanyan ! - Quoi ? - Quoicoubeh, Quoicoubeh, Quoicoubeh",            "Pierre n'amasse pas mousse.",
          "Mmmmmh ! Charal !",
          "Si le lion perd sa crinière, il ne rugit pas moins fort. - Proverbe africain",
          "Le vieil éléphant sait où trouver de l'eau.”,
          "C'est en essayant encore et encore que le singe apprend à bondir.",
          "Même le lion doit défendre lui-même contre les mouches."
        ]
    
    def citation_de_type_aleatoire(self):
        return random.choice(self.citations)

# Utilisation de la classe
mes_citations = Citation()
print(mes_citations.citation_de_type_aleatoire())
