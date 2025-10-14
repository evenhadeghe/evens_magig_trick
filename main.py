from magic_trick import MagicTrick
from utils import clear_screen, pause
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    print(Fore.CYAN + "🧠 Välkommen till Evens Magic Trick!\n")
    trick = MagicTrick()

    # Be användaren tänka på ett namn
    print("Tänk på ett namn från listan nedan... men säg det inte högt 😉")
    pause(2)

    for round_num in range(3):
        print(Fore.YELLOW + f"\nRunda {round_num + 1}")
        trick.show_cards()

        while True:
            try:
                choice = int(input(Fore.CYAN + "\nVilken kolumn är namnet i? (1, 2, 3): "))
                if choice in [1, 2, 3]:
                    break
                raise ValueError
            except ValueError:
                print(Fore.RED + "Skriv bara 1, 2 eller 3.")
        
        trick.regroup(choice)
        clear_screen()
        pause(0.5)

    print(Fore.GREEN + f"\n✨ Namnet du tänkte på är... {trick.cards[10]}! ✨" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
