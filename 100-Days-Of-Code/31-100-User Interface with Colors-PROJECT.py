import time, os

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

os.system('cls')

print(f"\t\t\t{RED}={LIGHT_WHITE}={BLUE}={END} Music App {BLUE}={LIGHT_WHITE}={RED}={END}\t\t\t\n")
print(f"\t\t{LIGHT_WHITE}RADIO GAGA{END}\n\t\tQueen")
print(f"{LIGHT_WHITE}PREV\n\t{GREEN}NEXT\n\t\t{PURPLE}PAUSE{END}\n")

time.sleep(10)
os.system('cls')

text = "WELCOME TO"
print(f"{LIGHT_WHITE}{text:^100}")
text = "--  ARMBOOK  --"
print(f"{BLUE}{text:^100}")
text = "Definitely not a rip off"
print(f"{END}{text:>100}")
text = "a certain other social"
print(f"{text:>100}")
text = "networking site"
print(f"{text:>100}")
text = "Honest."
print(f"{RED}{text:^100}")
text = "Username: "
UserInput = input(f"{LIGHT_WHITE}{text:^100}")
text = "Password: "
UserInput = input(f"{LIGHT_WHITE}{text:^100}")