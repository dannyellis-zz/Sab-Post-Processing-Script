#!/usr/bin/python

import sys
import os
import shutil
import glob

def main(argv):
    # Sab throws back 7 arguments, if there aren't 7 something went wrong so quit
    if (len(argv) < 7):
        print "Something went wrong. Fewer arguments than expected"
        return -1
    # Setting variables, these three are the only I care about
    origDir = argv[1]
    title = argv[3]
    category = argv[5]
    # Set the category name to have a capital letter
    category = category.title()
    # User defined mount point, changed this to the directory that
    # you want all your files to be saved (Movies, Music etc)
    # Mine is /mnt/raid/Movies for Movies, so I set it to /mnt/raid only!!!
    mountpoint = "/mnt/raid"
    
    # So if the path to the base Movies, Music, etc doesn't exist, make that first
    if not os.path.isdir(os.path.join(mountpoint, category)):
        os.mkdir(os.path.join(mountpoint, category))
        
    # Now set the destination folder for where you want to save this specific file    
    dest_folder = os.path.join(mountpoint, category, title)    
    # Copy over all the contents of the original folder to the new dir.
    shutil.copytree(origDir, dest_folder)

    # Loop to go through, remove some files I dont care about then
    # set the permissions for the files I keep
    for basename in os.listdir(dest_folder):
        if basename.endswith('.nfo') or basename.endswith('.sfv') or basename.endswith('.srr'):
            os.remove(os.path.join(dest_folder, basename))
        else:
            os.chmod(os.path.join(dest_folder, basename), 0755)
    
    # Lastly remove all the original files as we don't want it in two places
    # If you do want to keep originals, comment out this line
    shutil.rmtree(origDir)
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
