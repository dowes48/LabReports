walk_tree — README

This workspace includes `walk_tree.py` — a small utility to walk the directory tree.

Quick usage:

Windows PowerShell
```
python .\walk_tree.py --root . --out tree_walk.txt
```

Linux/macOS
```
python3 ./walk_tree.py --root . --out tree_walk.txt
```

Options:
- `--root` or `-r`: directory to walk (default: current directory)
- `--out` or `-o`: write output to file (if omitted, prints to stdout)
- `--max-depth` or `-d`: limit traversal depth (integer)

Example: write a shallow tree of just top-level files and folders:
```
python .\walk_tree.py -r . -o tree_walk.txt -d 1
```
