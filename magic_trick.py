from deck import Deck

class MagicTrick(Deck):
    def __init__(self):
        super().__init__()
        self.cards = self.draw_21()  # "cards" nu egentligen namn

    def show_cards(self):
        # Visa 21 namn i 3 kolumner
        print("\nHär är alla namn:\n")
        for i in range(0, 21, 3):
            print(f"{self.cards[i]:<20} {self.cards[i+1]:<20} {self.cards[i+2]}")

    def regroup(self, chosen_col: int):
        col1 = self.cards[0::3]
        col2 = self.cards[1::3]
        col3 = self.cards[2::3]

        if chosen_col == 1:
            self.cards = col2 + col1 + col3
        elif chosen_col == 2:
            self.cards = col1 + col2 + col3
        elif chosen_col == 3:
            self.cards = col1 + col3 + col2
        else:
            raise ValueError("Column must be 1, 2, or 3")
