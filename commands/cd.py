help = "Change directory. Usage: cd <dir>"

def run(args):
    import os
    if not args:
        print("Usage: cd <directory>")
        return
    try:
        os.chdir(args[0])
    except Exception as e:
        print(f"Error: {e}")