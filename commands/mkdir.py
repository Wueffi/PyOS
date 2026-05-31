import typing

command_help: str = 'Create a directory. Usage: mkdir <dir>'


def run(args: typing.Any) -> None:
    import os
    if not args:
        print('Usage: mkdir <dir>')
        return
    try:
        os.mkdir(args[0])
    except Exception as e:
        print(f'Error: {e}')
