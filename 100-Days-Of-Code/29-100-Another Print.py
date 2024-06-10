import random

BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

def RandomColors():
    Colors = random.choice([BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE])
    if Colors == BLACK:
        Colors = f"Black('and') {BLACK}and{RESET}"
    return Colors
TheColor = RandomColors()