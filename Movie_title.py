#!/usr/bin/python3
import re

pattern = r'(.*?) \((\d{4})\)$'

titles = [
    "Avengers (2021)",
    "The Mother (2023)",
    "Moana (2016)",
    "Sponge Bob (2020)",
    "Henry Danger (2014)",
    "Avatar (2009)",
]

for title in titles:
    match = re.match(pattern, title)
    if match:
        print(f"Valid title: {title}")
        print(f"Title: {match.group(1)}")
        print(f"Year: {match.group(2)}")
        print()
    else:
        print(f"Invalid title: {title}")
        print()
