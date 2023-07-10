#!/usr/bin/python3

import sys
import os.path
import markdown

def markdown2html(in_file, out_file):
    if not os.path.isfile(in_file):
        print(f"Missing {in_file}", file=sys.stderr)
        sys.exit(1)

    with open(in_file, 'r') as f:
        in_content = f.read()

    out_content = markdown.markdown(in_content)

    with open(out_file, 'w') as f:
        f.write(out_content)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    markdown2html(in_file, out_file)
    sys.exit(0)