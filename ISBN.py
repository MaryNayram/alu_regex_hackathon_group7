#!/usr/bin/python3

import re
pattern = r'^ISBN \d{3}\-\d{1}\-\d{3}\-\d{5}\-\d{1}$'
ISBN = input("ISBN xxx-x-xxx-xxxxx-x: ")

match = re.match(pattern, ISBN)

if match:
    print("This is a match")
else:
    print("This doesn't match")
