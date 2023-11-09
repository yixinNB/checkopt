import sys

import checkopt

print(sys.argv)
options, arguments = checkopt.checkopt("g help m|module=*")
print(options)
print(arguments)
