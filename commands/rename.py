import os
import typing

command_help: str = 'Rename a file. Usage: rename <old_file> <new_file>'


def run(args: typing.Any) -> None:
    if not args:
        print('Usage: rename <old_file> <new_file>')
        return

    if len(args) != 2:
        print('Usage: rename <old_file> <new_file>')
        return

    try:
        os.rename(args[0], args[1])
    except Exception as e:
        print(f'Error: {e}')
