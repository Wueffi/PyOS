import typing

command_help: str = 'List files in current directory.'


def run(_args: typing.Any) -> None:
    import os
    for f in os.listdir():
        print(f)
