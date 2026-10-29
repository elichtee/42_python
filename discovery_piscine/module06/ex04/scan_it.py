#!/opt/pyenv/shims/python

import re
import sys

#sys.argv is a list in Python that stores everything typed into the terminal to run the script.
#sys.argv[0] is always the name of the script itself.
#sys.argv[1] is the first parameter (your keyword).
#sys.argv[2] is the second parameter (your string).
if len(sys.argv) !=3:
	print("none")
	sys.exit()

keyword = sys.argv[1]
target_string = sys.argv[2]

#re.escape to handle special regex characters
scan_it = re.findall(re.escape(keyword),target_string)

if not scan_it:
	print("none")
else:
	print(len(scan_it))


