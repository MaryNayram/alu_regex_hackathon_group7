#!/usr/bin/python3

import re

pattern = r'^@\w+$'

twitter = input("Twitter username: ")

match = re.match(pattern, twitter)

if match:
    print("This is a match")
else:
    print("This isn't a match")
