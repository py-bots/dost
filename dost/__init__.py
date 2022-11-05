__version__ = '0.0.2'
__release_id__ = 2
__author__ = 'PyBOTs LLC'
__email__ = 'support@pybots.ai'
import os
__logfile__ = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'dost.log')

"""
DOST(friend) is a Python open-source library that helps you to write your code in a more readable and understandable way. And also help you in your python journey. Learn python in more practical way with DOST.
"""
import sys
import getopt

argument_list = sys.argv[1:]
short_options = "v=:i"
long_options = ["version", "info"]

try:
    arguments, values = getopt.getopt(
        argument_list, short_options, long_options)
    for current_argument, current_value in arguments:
        if current_argument in ("-v", "--version"):
            print(f"version : {__version__}")
            sys.exit(0)
        if current_argument in ("-i", "--info"):
            print(f"{__version__},{__release_id__}")
            sys.exit(0)
except getopt.error as err:
    print(str(err))
    sys.exit(2)
