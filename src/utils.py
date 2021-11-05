from colorama import init, Fore, Style
import datetime, os

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
dim = Style.DIM
r = Fore.RESET
def log(name, message):
    text_length = len(name) + len(message) + 2
    column_length = os.get_terminal_size().columns
    to_pad = column_length - text_length - 5
    date = str(datetime.datetime.now().strftime("%a %b %d %Y @ %I:%M:%S %p"))
    print(f"{name} {message}")