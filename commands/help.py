import os

help = """Show help for all commands."""

def run(args):
    from boot import load_commands
    commands = load_commands()
    print("Available commands:")
    for name in sorted(commands):
        mod = commands[name]
        doc = getattr(mod, "help", "")
        print(f"  {name:<10} {doc}")