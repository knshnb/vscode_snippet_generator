import os
import glob
import json
import sys

EXTENSIONS = {'.cpp', '.hpp'}
OUTPUT_FILE = 'cpp.json'


def create_snippet(file_path):
    name = os.path.splitext(os.path.basename(file_path))[0]
    with open(file_path, mode='r') as f:
        text = f.read()
    snippet = {
        'prefix': name,
        'body': text,
        'description': name,
    }
    return snippet


def create_snippets(dir_name):
    snippets = {}
    for file_path in glob.iglob(os.path.join(dir_name, '**', '*'), recursive=True):
        ext = os.path.splitext(file_path)[1]
        if os.path.isfile(file_path) and ext in EXTENSIONS:
            file_name = os.path.basename(file_path)
            snippets[file_name] = create_snippet(file_path)
    return snippets


if __name__ == '__main__':
    snippets = create_snippets(sys.argv[1])
    with open(OUTPUT_FILE, mode='w') as f:
        f.write(json.dumps(snippets, ensure_ascii=False, indent=4))
