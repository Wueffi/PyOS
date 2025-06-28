help = "Clear the screen."

def run(args):
    import os
    os.system('cls' if os.name == 'nt' else 'clear')