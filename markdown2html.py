#!/usr/bin/python3
"""
Markdown to HTML converter
"""

import sys
import re

def process_heading(line):
    """Process heading syntax"""
    level = line.count('#')
    content = line.strip('#').strip()
    return f"<h{level}>{content}</h{level}>"

def process_unordered_list(line):
    """Process unordered list syntax"""
    items = line.split('-')
    items = [item.strip() for item in items if item.strip()]
    html_list = "<ul>\n"
    for item in items:
        html_list += f"    <li>{item}</li>\n"
    html_list += "</ul>"
    return html_list

def process_ordered_list(line):
    """Process ordered list syntax"""
    items = line.split('*')
    items = [item.strip() for item in items if item.strip()]
    html_list = "<ol>\n"
    for item in items:
        html_list += f"    <li>{item}</li>\n"
    html_list += "</ol>"
    return html_list

def process_paragraph(line):
    """Process paragraph syntax"""
    return f"<p>\n    {line}\n</p>"

def process_bold(line):
    """Process bold syntax"""
    line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
    line = re.sub(r"__(.*?)__", r"<em>\1</em>", line)
    return line

def process_special(line):
    """Process special syntax"""
    line = re.sub(r"\[\[(.*?)\]\]", lambda x: x.group(1).lower().encode("utf-8").hex(), line)
    line = re.sub(r"\(\((.*?)\)\)", lambda x: x.group(1).replace("c", "").replace("C", ""), line)
    return line

def process_file(markdown_file, html_file):
    """Process the markdown file and convert it to HTML"""
    with open(markdown_file, 'r') as md:
        markdown_lines = md.readlines()

    html_lines = []
    for line in markdown_lines:
        line = line.rstrip('\n')
        if line.startswith('#'):
            html_lines.append(process_heading(line))
        elif line.startswith('-'):
            html_lines.append(process_unordered_list(line))
        elif line.startswith('*'):
            html_lines.append(process_ordered_list(line))
        elif line.strip() == '':
            html_lines.append('')
        else:
            line = process_bold(line)
            line = process_special(line)
            html_lines.append(process_paragraph(line))

    with open(html_file, 'w') as html:
        html.writelines(html_lines)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    try:
        process_file(markdown_file, html_file)
        sys.exit(0)
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
