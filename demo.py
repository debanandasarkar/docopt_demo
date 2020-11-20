# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: docopt.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [--arg4=<arg4>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[--arg4=<arg4>]   Takes any value (this is the custom optional option)
"""

from docopt import docopt

def main(docstring):
    opt = docopt(docstring)
    print(opt)
    print(type(opt))

if __name__ == "__main__":
    main(__doc__)
