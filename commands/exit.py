import typing

command_help: str = 'Exit PyOS.'


def run(_args: typing.Any) -> None:
    print('Goodbye!')
    exit(0)
