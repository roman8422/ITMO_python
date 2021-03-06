import os

def du(path, recursive=True):
    size = 4096 # dir size itself
    paths_list = os.listdir(path)
    for subpath in paths_list:
        path_to_check = os.path.join(path, subpath)
        if not os.path.isdir(path_to_check):
            size += os.path.getsize((path_to_check))
        elif os.path.isdir(path_to_check):
            if recursive:
                size += du(path_to_check, recursive=True)

    return size

if __name__ == "__main__":
    print("Test of dir functino:")
    # to test dir python3 was copied from /usr/share/
    dir = '../python3'
    print("Dir {dir} size is - {size}".format(dir=dir, size=du(dir, recursive=False)))
    print()
    print("Dir {dir} size is - {size}".format(dir=dir, size=du(dir)))
