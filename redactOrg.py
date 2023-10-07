#!/usr/bin/env python3

from orgmunge import Org
import re
from random import choices
import sys

# Redacts the input file by randomly choosing words from the lipsum file
# (can be Lorem Ipsum text or anything you want) to replace words in the
# input file's heading titles, body text and property values.

try:
    lipsum_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
except IndexError:
    print(f"Usage: {sys.argv[0]} /path/to/lipsum_file /path/to/input_file /path/to/output_file")

with open(lipsum_file, 'r') as IN:
    LIPSUM = re.split(r'\s+', IN.read().strip())

def fudge(text):
    if text is None: return None
    if text == '': return ''
    num_words = len(re.split(r'\s+', text.strip()))
    return ' '.join(choices(LIPSUM, k=num_words))

org_file = Org(input_file)
for heading in org_file.get_all_headings():
    heading.body = fudge(heading.body)
    heading.headline.title = fudge(heading.title)
    heading.headline.tags = [fudge(tag) for tag in heading.headline.tags] if heading.headline.tags else None
    heading.properties = {fudge(k): fudge(v) for (k, v) in heading.properties.items()}
    if heading.drawers:
        for drawer in heading.drawers:
            if drawer.name == 'LOGBOOK':
                drawer.contents = [fudge(text) if not re.search(r'^(?:-|CLOCK)', text) else text
                                            for text in drawer.contents]
org_file.metadata = {k: [fudge(x) for x in v] for k, v in org_file.metadata.items()}
org_file.initial_body = fudge(org_file.initial_body)
org_file.write(output_file)
