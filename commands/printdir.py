import typing

command_help: str = 'Print working directory.'


def run(_args: typing.Any) -> None:
    import os
    print(os.getcwd())
