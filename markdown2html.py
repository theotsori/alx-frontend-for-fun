#!/usr/bin/python3

import sys
import os.path
import re
import hashlib


def convert_heading(line):
    """
    Converts a Markdown heading to HTML heading tags.
    """
    match = re.match(r'^(#+)\s*(.*)$', line)
    if match:
        heading_level = len(match.group(1))
        heading_text = match.group(2).strip()
        return f"<h{heading_level}>{heading_text}</h{heading_level}>"
    else:
        return line


def convert_unordered_list(line):
    """
    Converts a Markdown unordered list item to HTML list item tags.
    """
    if re.match(r'^-\s+', line):
        list_item = re.sub(r'^-\s+', '', line)
        return f"<li>{list_item}</li>"
    else:
        return line


def convert_ordered_list(line):
    """
    Converts a Markdown ordered list item to HTML list item tags.
    """
    if re.match(r'^\*\s+', line):
        list_item = re.sub(r'^\*\s+', '', line)
        return f"<li>{list_item}</li>"
    else:
        return line


def convert_paragraph(line):
    """
    Converts a Markdown paragraph to HTML paragraph tags.
    """
    if line.strip() == "":
        return line
    else:
        return f"<p>\n{line}\n</p>\n"


def convert_bold(line):
    """
    Converts Markdown bold and emphasis syntax to HTML tags.
    """
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'__(.*?)__', r'<em>\1</em>', line)
    return line


def convert_md5(line):
    """
    Converts Markdown content enclosed in double
    square brackets to its MD5 hash.
    """
    line = re.sub(
        r'\[\[(.*?)\]\]',
        lambda match: hashlib.md5(match.group(1).encode()).hexdigest(),
        line
    )
    return line


def remove_letter_c(line):
    """
    Removes all occurrences of the letter 'c'
    (case-insensitive) from the content.
    """
    line = re.sub(
        r'\(\((.*?)\)\)',
        lambda match: match.group(1).replace('c', ''),
        line,
        flags=re.IGNORECASE
    )
    return line


def markdown2html(in_file, out_file):
    """
    Converts a Markdown file to HTML format.
    """
    if not os.path.isfile(in_file):
        print(f"Missing {in_file}", file=sys.stderr)
        sys.exit(1)

    with open(in_file, 'r') as md_file:
        markdown_lines = md_file.readlines()

    html_lines = []
    for line in markdown_lines:
        line = convert_heading(line)
        line = convert_unordered_list(line)
        line = convert_ordered_list(line)
        line = convert_paragraph(line)
        line = convert_bold(line)
        line = convert_md5(line)
        line = remove_letter_c(line)
        html_lines.append(line)

    with open(out_file, 'w') as html_file:
        html_file.writelines(html_lines)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(
            'Usage: ./markdown2html.py README.md README.html',
            file=sys.stderr
        )
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    markdown2html(in_file, out_file)
    sys.exit(0)
