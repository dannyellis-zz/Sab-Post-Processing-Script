#!/usr/bin/python

import sys
import os
import shutil
import glob

def main(argv):
    if (len(argv) < 7):
        print "Something went wrong. Fewer arguments than expected"
        return -1
    origDir = argv[1]
    title = argv[3]
    category = argv[5]
    category = category.title()
    mountpoint = "/mnt/raid"
    
    if not os.path.isdir(os.path.join(mountpoint, category)):
        os.mkdir(os.path.join(mountpoint, category))
    dest_folder = os.path.join(mountpoint, category, title)    
    shutil.copytree(origDir, dest_folder)

    for basename in os.listdir(dest_folder):
        if basename.endswith('.nfo') or basename.endswith('.sfv') or basename.endswith('.srr'):
            os.remove(os.path.join(dest_folder, basename))
        else:
            os.chmod(os.path.join(dest_folder, basename), 0755)
    
    shutil.rmtree(origDir)
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
