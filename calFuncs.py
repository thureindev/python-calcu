import math


# calculation functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def floor_division(n1, n2):
    return n1 // n2


def modulus(n1, n2):
    return n1 % n2


def exponent(n1, n2):
    return n1 ** n2


#    #    single number operations: opts needs only 1 num input
def square(n1):
    return exponent(n1, 2)


def cube(n1):
    return exponent(n1, 3)


def square_root(n1):
    return math.sqrt(n1)


def floor_num(n1):
    return math.floor(n1)


def round_num(n1):
    return round(n1)


# format funcs
def format_add(text, num):
    return f"{text} + {num}"


def format_substract(text, num):
    return f"{text} - {num}"


def format_multiply(text, num):
    return f"{text} x {num}"


def format_division(text, num):
    return f"{text} / {num}"


def format_floor_division(text, num):
    return f"floor({text} / {num})"


def format_modulus(text, num):
    return f"({text} mod {num})"


def format_exponent(text, num):
    return f"({text})^{num}"


#    #    single number operations: opts needs only 1 num input
def format_square(text):
    return f"({text})^2"


def format_cube(text):
    return f"({text})^3"


def format_sqrt(text):
    return f"sqrt({text})"


def format_floor_num(text):
    return f"floor({text})"


def format_round_num(text):
    return f"round({text})"


# export opeartions
operations = {
    "+": add,
    "-": subtract,
    "x": multiply,
    "/": division,
    "//": floor_division,
    "mod": modulus,
    "^": exponent,
    "^2": square,
    "^3": cube,
    "sqrt": square_root,
    "flor": floor_num,
    "rond": round_num
}
single_num_operations = [
    "^2",
    "^3",
    "sqrt",
    "flor",
    "rond"
]

format_operations = {
    "+": format_add,
    "-": format_substract,
    "x": format_multiply,
    "/": format_division,
    "//": format_floor_division,
    "mod": format_modulus,
    "^": format_exponent,
    "^2": format_square,
    "^3": format_cube,
    "sqrt": format_sqrt,
    "flor": format_floor_num,
    "rond": format_round_num
}
