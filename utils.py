# utils.py – Hjälpfunktioner

import os
import time

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def pause(sec=1):
    time.sleep(sec)
