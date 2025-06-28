# WAFCAT :heart:

help = "Print file contents. Usage: cat <file>"

def run(args):
    if not args:
        print("Usage: cat <file>")
        return
    try:
        with open(args[0], 'r') as f:
            print(f.read())
    except Exception as e:
        print(f"Error: {e}")