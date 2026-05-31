import typing

command_help: str = 'Get current user'


def run(_args: typing.Any) -> None:
    import getpass
    print(getpass.getuser())
