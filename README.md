manage-to-ipython
=========================

A configuration to run IPython in a Django virtual environment.

When developing a Django project in a virtual environment with --no-site-packages, IPython does not execute correctly unless it is also installed in the virtual environment.  If you do **not** want to install IPython into every virtual environment, you can trying running the system installed version of IPython while in a virtual environment.  This will hit two issues:

  - IPython can not see all the packages necessary to run IPython
  - IPython can not see the project settings file for a particular Django project

## Fixing IPython access to missing packages Virtual environments

Access to the missing packages can be fixed by adding two directories to the sys.path before starting IPython.  This can be done by adding the following lines to the file `/usr/bin/ipython` above the call to `launch_new_instance()`:

    import sys
    if "/usr/lib/python2.7/dist-packages" not in sys.path:
        sys.path.append("/usr/lib/python2.7/dist-packages")
    if "/usr/lib/pymodules/python2.7" not in sys.path:
        sys.path.append("/usr/lib/pymodules/python2.7")

## Fix IPython access to the Django project.settings.py configuration file

The manage.py script created by django-admin.py provides a perfect template to set the environment for IPython as it contains the project specific path to the settings.py file.  It is a hassle to create a custom IPython configuration file for each Django project.

The `manage_to_ipython.py` script creates an executable file `runipython.py` that runs the system-wide installed IPython in a local Django project.settings file enviroment.  The script reads the local project manage.py file and creates a new file called `runipython.py`.

The `manage_to_ipython.py`, cd to the Django top-level project directory, then execute the script.

    $ cd <project_dir>
    $ python manage_to_ipython.py

To run IPython, simply type:

    $ ./runipython.py


