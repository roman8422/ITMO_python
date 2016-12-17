"""
This module require binaryornot module installed
"""
import os
binaryornot_installed = False
try:
    from binaryornot.check import is_binary
    binaryornot_installed = True
except ImportError:
    print("""
ATTENTION:
You don't have binaryornot module installed. Errors will arise when trying to grep over binary files.
To get best experience, please install it with the following command:
pip install binaryornot
    """)

def grep(dir, str, recursive=False, ignorecase=False):
    paths_list = os.listdir(dir)
    for subpath in paths_list:
        name_to_check = subpath
        if ignorecase:
            name_to_check = subpath.lower()
            str = str.lower()

        full_path = os.path.join(dir, subpath)
        # print("Checking", full_path)
        if str in name_to_check:
            print("Filename matches template:", full_path)

        if not os.path.isdir(full_path):
            file_is_binary = False
            if binaryornot_installed:
                file_is_binary = is_binary(full_path)

            if not file_is_binary:
                with open(full_path, 'r') as f:
                    line_num = 0
                    for line in f:
                        line_num += 1
                        line_to_compare = line
                        if ignorecase:
                                    line_to_compare = line_to_compare.lower()

                        if str in line_to_compare:
                            print("Line number {num} in file {path} matches template: {line}".format(num=line_num, path=full_path, line=line.strip()))

        if os.path.isdir(full_path):
            if recursive:
                grep(full_path, str, recursive, ignorecase)

    return 0

if __name__ == "__main__":
    print("\nTest of grep function:")
    dir = '../python3'

    str = 'Pyt'
    print('\nstr =', str)
    print(grep(dir, str, ignorecase=True))

    str = 'ValueError'
    print('\nstr =', str)
    print(grep(dir, str, ignorecase=True, recursive=True))
