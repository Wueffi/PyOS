import typing

command_help: str = 'Clear the screen.'


def run(_args: typing.Any) -> None:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
