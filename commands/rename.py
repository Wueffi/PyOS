import os
import typing

command_help: str = 'Rename a file. Usage: rename <old_file> <new_file>'


def run(args: typing.Any) -> None:
    if not args:
        print('Usage: rename <old_file> <new_file>')
        return

    target = args[0]
    if os.path.isdir(target):
        print('Usage: rename <old_file> <new_file>')
        return
    else:
        try:
            with open(target, 'r') as file:
                content = file.read()
            os.remove(target)
        except Exception as e:
            print(f'Error: {e}')
            return

    try:
        with open(args[1], 'w') as file:
            file.write(content)
    except Exception as e:
        print(f'Error: {e}')
