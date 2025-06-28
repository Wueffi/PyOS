help = "Create a directory. Usage: mkdir <dir>"

def run(args):
    import os
    if not args:
        print("Usage: mkdir <dir>")
        return
    try:
        os.mkdir(args[0])
    except Exception as e:
        print(f"Error: {e}")