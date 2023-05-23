#!/usr/bin/python3

import re

pattern = r'^#[0-9A-Fa-f]{6}$'
hex_color = input("hex color: ")

match = re.match(pattern, hex_color)

if match:
    print("This is a match")
else:
    print("This isn't a match")
