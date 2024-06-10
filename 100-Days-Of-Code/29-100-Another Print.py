import random, os, time

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
    elif Colors == RED:
        Colors = f"Red('and') {RED}and{RESET}"
    elif Colors == GREEN:
        Colors = f"Green('and') {GREEN}and{RESET}"
    elif Colors == YELLOW:
        Colors = f"Yellow('and') {YELLOW}and{RESET}"
    elif Colors == BLUE:
        Colors = f"Blue('and') {BLUE}and{RESET}"
    elif Colors == MAGENTA:
        Colors = f"Magenta('and') {MAGENTA}and{RESET}"
    elif Colors == CYAN:
        Colors = f"Cyan('and') {CYAN}and{RESET}"
    elif Colors == WHITE:
        Colors = f"White('and') {WHITE}and{RESET}"
    else:
        print(f"{RED}Achtung!{RESET}")
        quit()
    return Colors

time.sleep(5)
os.system("cls")
print("sds")