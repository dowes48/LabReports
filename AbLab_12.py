
TARGETDIR = r'./AbLab_Rpts'

form_feed = '\f'
form_count = 0
line_count = 0


import os

def process_line(f_in):
    global line_count, form_count
    for line in f_in:
        line_count += 1
        if form_feed in line:
            form_count += 1

def walk(dirname):
    global form_count, line_count
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            file_in = open(path, 'r')
            process_line(file_in)
            print(f"  File: {path}  Lines: {line_count}  Forms: {form_count}")
            form_count = 0
            line_count = 0
            file_in.close()

        elif os.path.isdir(path):
            print("\nDirectory: ................." + path)
            walk(path)

walk(TARGETDIR)

