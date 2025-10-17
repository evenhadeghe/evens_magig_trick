 Evens Magic Trick

Detta projekt är ett Python-program som utför det klassiska 21-korts-tricket, men med namn istället för spelkort.  
Användaren tänker på ett namn från listan och anger tre gånger vilken kolumn namnet ligger i.  
Programmet gissar sedan rätt namn.


Funktioner
- Dela upp 21 namn i tre kolumner
- Användarinmatning för val av kolumn
- Automatisk beräkning av vilket namn användaren tänker på
- Färg i terminalen via `colorama`
- Enkel testning med `pytest`

Struktur
evens_magic_trick/
├── deck.py
├── magic_trick.py
├── main.py
├── utils.py
├── test_deck.py
└── README.md

Bibliotek
- Standard: `random`, `os`, `time`
- Externt: `colorama`
- Testning: `pytest`

Installation och körning
1. Klona projektet  
   ```bash
   git clone <https://github.com/evenhadeghe/evens_magig_trick.git>
   cd evens_magic_trick

Skapa och aktivera virtuell miljö
- python3 -m venv venv
- source venv/bin/activate

Installera beroenden
- pip install colorama pytest

Kör programmet
- python main.py

Testning
Kör testet med:
- pytest