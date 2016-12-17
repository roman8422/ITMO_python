import os

def grep(dir, str, recursive=False, ignorecase=False):
    paths_list = os.listdir(dir)
    for subpath in paths_list:
        name_to_check = subpath
        if ignorecase:
            name_to_check = subpath.lower()
            str = str.lower()

        full_path = os.path.join(dir, subpath)
        if str in name_to_check:
            print("Filename matches template:", full_path)
        if os.path.isdir(full_path):
            if recursive:
                grep(full_path, str, recursive, ignorecase)

    return 0

if __name__ == "__main__":
    print("\nTest of grep functino:")
    dir = 'python3'

    str = 'Pyt'
    print('\nstr =', str)
    print(grep(dir, str, ignorecase=True))

    str = 'yth'
    print('\nstr =', str)
    print(grep(dir, str, ignorecase=True, recursive=True))
