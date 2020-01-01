import os

paths = []


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
    find_dir(suffix, path)
    print("paths", paths)
    return paths


def find_dir(suffix, path):
    if not os.path.isfile(path):
        list_dir = os.listdir(path)
        for dir in list_dir:
            if os.path.isfile(dir):
                if dir.endswith(suffix):
                    paths.append(path+'\\'+dir)
            else:
                find_dir(suffix, path+"\\"+dir)
    elif path.endswith(suffix):
        paths.append(path)

find_files(".c", "C:\\Arun\\Work\\DS\\Show me the DS\\testdir")
