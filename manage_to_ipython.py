#!/usr/bin/env python
import os, stat
import sys

# Define input and outfiles
INFILENAME = "manage.py"
OUTFILENAME = "runipython.py"

def manage_to_runipython():
    # open input file
    try:
        managefile = open(INFILENAME, 'r')
    except IOError:
        print "File open error!  Check {} exists.".format(INFILENAME)
        sys.exit()
    else:
        lines = managefile.readlines()
        
    # open output file
    try:
        outfile = open(OUTFILENAME, 'w')
    except IOError:
        print "File open error!  Could not open {} for writing.".format(OUTFILENAME)
        sys.exit()
    else:
        # process input file
        for line in lines:
            # drop these lines
            if "django.core.management" in line:
                continue
            if "execute_from_command" in line:
                continue
            
            # inject this lines ...
            if "import sys" in line:
                # ... after import sys
                outfile.write("from subprocess import call\n")
                
            outfile.write(line)

        # add line to call ipython in new environment
        outfile.write('call(["ipython"])')

        # clean up
        outfile.close()
        
        # set file mode
        # stat.S_IRWXU: Read, write, and execute by owner.
        # stat.S_IRGRP: Read by group.
        # stat.S_IXGRP: Execute by group.
        # stat.S_IROTH: Read by others.
        # stat.S_IXOTH: Execute by others.
        os.chmod(OUTFILENAME, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH )
        
if __name__ == "__main__":
    manage_to_runipython()