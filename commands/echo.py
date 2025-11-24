import typing

command_help = 'Echo the input arguments to the output. Usage: echo [args...]'

def run(args: typing.Any) -> None:
    print(args)
