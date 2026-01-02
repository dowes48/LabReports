#!/usr/bin/env python3
"""
walk_tree.py — simple directory tree walker
Usage:
    python walk_tree.py [--root ROOT_DIR] [--out OUT_FILE] [--max-depth N]

If --out is provided the tree is written to that file, otherwise printed to stdout.
"""
import os
import argparse

def format_tree(root, max_depth=None):
    lines = []
    root = os.path.abspath(root)
    prefix_len = len(root) + 1
    for dirpath, dirnames, filenames in os.walk(root):
        depth = dirpath.count(os.sep) - root.count(os.sep)
        if max_depth is not None and depth > max_depth:
            # prevent walking deeper
            dirnames[:] = []
            continue
        indent = '    ' * depth
        rel = dirpath[prefix_len:] if dirpath.startswith(root) else dirpath
        lines.append(f"{indent}{os.path.basename(dirpath) or dirpath}")
        for f in sorted(filenames):
            lines.append(f"{indent}    {f}")
    return "\n".join(lines)

def main():
    p = argparse.ArgumentParser(description='Walk directory tree and print/save a simple tree view')
    p.add_argument('--root', '-r', default='.', help='Root directory to walk')
    p.add_argument('--out', '-o', help='Output file path (optional)')
    p.add_argument('--max-depth', '-d', type=int, help='Maximum depth to traverse')
    args = p.parse_args()

    tree_text = format_tree(args.root, args.max_depth)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as fh:
            fh.write(tree_text)
        print(f"Wrote tree for {args.root} to {args.out}")
    else:
        print(tree_text)

if __name__ == '__main__':
    main()
