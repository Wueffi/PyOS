help = "List files in current directory."

def run(args):
    import os
    for f in os.listdir():
        print(f)