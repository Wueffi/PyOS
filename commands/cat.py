import typing

command_help: str = 'Print file contents. Usage: cat <file>'


def run(args: typing.Any) -> None:
    if not args:
        print('Usage: cat <file>')
        return
    try:
        with open(args[0], 'r') as f:
            print(f.read())
    except Exception as e:
        print(f'Error: {e}')
