from cx_Freeze import setup, Executable

setup(
    name = "order",
    version = "0.1",
    description = "Blackjack",
    executables = [Executable("make_order.py")]
)