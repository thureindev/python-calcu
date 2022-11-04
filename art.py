# import only system from os
from os import system, name


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def display(history="___", result="AC"):
    logo = f"""
 __________________________________________
|  ______________________________________  |\\
| | Python-Calcu by thureindev           | |\\
| |                                      | |\\
| | {history}
| |
| |             {result}
| |                                      | |\\
| |______________________________________| |\\
|  ___ ___ ___   ___   ____   ____   ____  |\\
| | 7 | 8 | 9 | | + | | AC | | .. | | .. | |\\
| | 4 | 5 | 6 | |___| |____| |____| |____| |\\
| | 1 | 2 | 3 | | - | |expo| |sqrt| | .. | |\\
| | . | 0 | = | |___| |____| |____| |____| |\\
| '---'---'---' | x | | ^2 | | ^3 | |flor| |\\
|               |___| |____| |____| |____| |\\
|               | / | | // | | mod| |rond| |\\
|               |___| |____| |____| |____| |\\
|                                          |\\
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT\\
"""
    clear()
    print(logo)


print_display = display
