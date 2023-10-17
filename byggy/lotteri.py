
import random 

class Lotteri:
    
    def __init__(self):
        self.list_vinster = [
            "Byggy",
            "AK 47",
            "Joel Swartling",
            "A pile of Bones",
            "20IQ",
            "20 Laxar",
            "En dejt med Björkman",
            "Elias Öl",
            "toffler",
            "Du får slå lill Mattias",
            "cs skins",
            "Queen's strumpor",
            "cinnamon roll plush",
            "stål trimer",
        ]
        
    def get_vinst(self):
        slumptal = random.randint(0, 19)
        return self.list_vinster[slumptal]        