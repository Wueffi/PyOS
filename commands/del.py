import typing

command_help: str = 'Delete file or directory. Usage: del <file/dir>'


def run(args: typing.Any) -> None:
    import os
    if not args:
        print('Usage: del <file/dir>')
        return
    target = args[0]
    if os.path.isdir(target):
        try:
            os.rmdir(target)
        except Exception as e:
            print(f'Error: {e}')
    else:
        try:
            os.remove(target)
        except Exception as e:
            print(f'Error: {e}')
