import os
import importlib
import pkgutil
import types

COMMANDS_PACKAGE = 'commands'


def load_commands() -> dict[str, types.ModuleType]:
    commands: dict[str, types.ModuleType] = {}
    package = importlib.import_module(COMMANDS_PACKAGE)
    for loader, name, is_pkg in pkgutil.iter_modules(package.__path__):
        if name.startswith('_'):
            continue
        mod = importlib.import_module(f'{COMMANDS_PACKAGE}.{name}')
        if hasattr(mod, 'run'):
            commands[name] = mod
    return commands


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Booting PyOS...')
    commands = load_commands()
    print(f'Found commands ({len(commands)}): {", ".join(sorted(commands))}')

    while True:
        try:
            cmdline = input(f'{os.getcwd()} > ').strip()
            if not cmdline:
                continue
            parts = cmdline.split()
            name, args = parts[0], parts[1:]
            if name in commands:
                if name == 'exit':
                    commands[name].run(args)
                    break
                commands[name].run(args)
            else:
                print(f'Unknown command: {name}')
        except KeyboardInterrupt:
            print('\nUse \'exit\' to quit.')


if __name__ == '__main__':
    main()
