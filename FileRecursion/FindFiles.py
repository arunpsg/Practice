import os




def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths = []

    if not path or path == " ":
        print("Please enter a valid Path")
        return "Please enter a valid Path"
    find_dir(suffix, path, paths)
    print("paths", paths)
    return paths


def find_dir(suffix, path, paths):
    try:
        if not os.path.isfile(path):
            list_dir = os.listdir(path)
            for inner_dir in list_dir:
                if os.path.isfile(inner_dir):
                    if inner_dir.endswith(suffix):
                        paths.append(os.path.join(inner_dir))
                else:
                    find_dir(suffix, path + "\\" + inner_dir, paths)
        elif path.endswith(suffix):
            paths.append(path)
    except FileNotFoundError:
        print("Please enter a valid Path")

# test cases
find_files(".c", "C:\\DS\\Show me the DS\\testdir")
# Expected output :
# paths ['C:\\Show me the DS\\testdir\\subdir1\\a.c', 'C:\\Show me the DS\\testdir\\subdir3\\subsubdir1\\b.c', 'C:\\Show me the DS\\testdir\\subdir5\\a.c', 'C:\\Show me the DS\\testdir\\t1.c']
find_files(".c", "C:\\ABC")
# Expected output :
# Please enter a valid Path
# paths []
find_files(".c", "")
# Expected output :
# Please enter a valid Path
