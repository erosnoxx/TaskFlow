import os

def print_tree(startpath: str, ignore_dirs: set, prefix: str = ''):
    entries = os.listdir(startpath)
    
    entries = [entry for entry in entries if entry not in ignore_dirs]

    for i, entry in enumerate(entries):
        path = os.path.join(startpath, entry)
        
        if os.path.isdir(path):
            connector = '├── ' if i < len(entries) - 1 else '└── '
            print(f"{prefix}{connector}{entry}/")
            print_tree(path, ignore_dirs, prefix + ('│   ' if i < len(entries) - 1 else '    '))
        else:
            print(f"{prefix}├── {entry}")

if __name__ == "__main__":
    project_directory = '.'
    ignore_dirs = {'.git', 'venv', '__pycache__', '.gitignore', '.vscode', 'tree.py'}

    print_tree(project_directory, ignore_dirs)
