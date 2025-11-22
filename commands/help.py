import typing

command_help: str = 'Show help for all commands.'


def run(_args: typing.Any) -> None:
    from boot import load_commands
    commands = load_commands()
    print('Available commands:')
    for name in sorted(commands):
        mod = commands[name]
        doc = getattr(mod, 'command_help', '')
        print(f'  {name:<10} {doc}')
