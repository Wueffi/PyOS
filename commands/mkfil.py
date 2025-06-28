help = "Create an empty file. Usage: mkfil <file>"


def run(args):
    if not args:
        print("Usage: touch <file>")
        return
    try:
        open(args[0], 'a').close()
    except Exception as e:
        print(f"Error: {e}")