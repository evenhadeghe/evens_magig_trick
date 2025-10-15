# deck.py – Hanterar listan med namn 
import random

class Deck:
    def __init__(self):
        # Här lägger du in namn från din klass (eller påhittade)
        self.names = [
            "Adam", "Vendela", "Viktor", "Mike", "Emma", "Emmy", "Bellika",
            "Ali", "Gabriella", "Harris", "Elvira", "Leonard", "Allan", "Constantine",
            "Nicklas", "Patrik", "Nahuel", "Kevin", "Youssef", "Nick", "David"
        ]
        random.shuffle(self.names)  # Blanda listan

    def draw_21(self):
        return self.names[:21]
