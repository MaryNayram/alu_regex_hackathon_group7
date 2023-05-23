#!/usr/bin/python3

import re


pattern = r'^\d{2}\-[a-zA-Z]{3}\-\d{4}$'


date = input("Enter date in this format 'dd-MMM-yyyy': ")


match = re.match(pattern, date)


if match:

    print("This is a match")

else:

    print("This isn't a match")
