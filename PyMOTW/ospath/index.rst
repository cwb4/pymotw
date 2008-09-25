==============
os.path
==============
.. module:: os.path
    :synopsis: Parse, build, test, and otherwise work on file names and paths.

:Module: os.path
:Purpose: Parse, build, test, and otherwise work on file names and paths.
:Python Version: 1.4 and later
:Abstract:

    Use os.path for platform-independent manipulation of file names.

Description
===========

Writing code to work with files on multiple platforms is easy using the
functions included in the os.path module. Even programs not intended to be
ported between platforms should use os.path to make parsing path names
reliable.

Parsing Paths
=============

The first set of functions in os.path can be used to parse strings
representing filenames into their component parts. It is important to realize
that these functions do not depend on the paths actually existing. They
operate solely on the strings.

Path parsing depends on a few variable defined in the os module:

* os.sep - The separator between portions of the path (e.g., "/").

* os.extsep - The separator between a filename and the file "extension" (e.g.,
  ".").

* os.pardir - The path component that means traverse the directory tree up one
  level (e.g., "..").

* os.curdir - The path component that refers to the current directory (e.g.,
  ".").

* split() breaks the path into 2 separate parts and returns the tuple. The
  second element is the last component of the path, and the first element is
  everything that comes before it.

::

    import os.path

    for path in [ '/one/two/three', 
                  '/one/two/three/',
                  '/',
                  '.',
                  '']:
        print '"%s" : "%s"' % (path, os.path.split(path))

::

    $ python ospath_split.py
    "/one/two/three" : "('/one/two', 'three')"
    "/one/two/three/" : "('/one/two/three', '')"
    "/" : "('/', '')"
    "." : "('', '.')"
    "" : "('', '')"

basename() returns a value equivalent to the second part of the split() value.

::

    import os.path

    for path in [ '/one/two/three', 
                  '/one/two/three/',
                  '/',
                  '.',
                  '']:
        print '"%s" : "%s"' % (path, os.path.basename(path))

::

    $ python ospath_basename.py
    "/one/two/three" : "three"
    "/one/two/three/" : ""
    "/" : ""
    "." : "."
    "" : ""

dirname() returns the first path of the split path:

::

    import os.path

    for path in [ '/one/two/three', 
                  '/one/two/three/',
                  '/',
                  '.',
                  '']:
        print '"%s" : "%s"' % (path, os.path.dirname(path))

::

    $ python ospath_dirname.py
    "/one/two/three" : "/one/two"
    "/one/two/three/" : "/one/two/three"
    "/" : "/"
    "." : ""
    "" : ""

splitext() works like split() but divides the path on the extension separator,
rather than the directory names.

::

    import os.path

    for path in [ 'filename.txt', 'filename', '/path/to/filename.txt', '/', '' ]:
        print '"%s" :' % path, os.path.splitext(path)

::

    $ python ospath_splitext.py
    "filename.txt" : ('filename', '.txt')
    "filename" : ('filename', '')
    "/path/to/filename.txt" : ('/path/to/filename', '.txt')
    "/" : ('/', '')
    "" : ('', '')

commonprefix() takes a list of paths as an argument and returns a single
string that represents a common prefix present in all of the paths. The value
may represent a path that does not actually exist, and the path separator is
not included in the consideration, so the prefix might not stop on a separator
boundary.

::

    import os.path

    paths = ['/one/two/three/four',
             '/one/two/threefold',
             '/one/two/three/',
             ]
    print paths
    print os.path.commonprefix(paths)

::

    $ python ospath_commonprefix.py
    ['/one/two/three/four', '/one/two/threefold', '/one/two/three/']
    /one/two/three

Building Paths
==============

Besides taking existing paths apart, you will frequently need to build paths
from other strings.

To combine several path components into a single value, use join():

::

    import os.path

    for parts in [ ('one', 'two', 'three'),
                   ('/', 'one', 'two', 'three'),
                   ('/one', '/two', '/three'),
                   ]:
        print parts, ':', os.path.join(*parts)

::

    $ python ospath_join.py
    ('one', 'two', 'three') : one/two/three
    ('/', 'one', 'two', 'three') : /one/two/three
    ('/one', '/two', '/three') : /three

It's also easy to work with paths that include "variable" components that can
be expanded automatically. For example, expanduser() converts the tilde (~)
character to a user's home directory.

::

    import os.path

    for user in [ '', 'dhellmann', 'postgres' ]:
        lookup = '~' + user
        print lookup, ':', os.path.expanduser(lookup)

::

    $ python ospath_expanduser.py
    ~ : /Users/dhellmann
    ~dhellmann : /Users/dhellmann
    ~postgres : /var/empty

expandvars() is more general, and expands any shell environment variables
present in the path.

::

    import os.path
    import os

    os.environ['MYVAR'] = 'VALUE'

    print os.path.expandvars('/path/to/$MYVAR')

::

    $ python ospath_expandvars.py
    /path/to/VALUE

Normalizing Paths
=================

Paths assembled from separate strings using join() or with embedded variables
might end up with extra separators or relative path components. Use normpath()
to clean them up:

::

    import os.path

    for path in [ 'one//two//three', 
                  'one/./two/./three', 
                  'one/../one/two/three',
                  ]:
        print path, ':', os.path.normpath(path)

::

    $ python ospath_normpath.py
    one//two//three : one/two/three
    one/./two/./three : one/two/three
    one/../one/two/three : one/two/three

To convert a relative path to a complete absolute filename, use abspath().

::

    import os.path

    for path in [ '.', '..', './one/two/three', '../one/two/three']:
        print '"%s" : "%s"' % (path, os.path.abspath(path))

::

    $ python ospath_abspath.py
    "." : "/Users/dhellmann/Documents/PyMOTW/in_progress/ospath"
    ".." : "/Users/dhellmann/Documents/PyMOTW/in_progress"
    "./one/two/three" : "/Users/dhellmann/Documents/PyMOTW/in_progress/ospath/one/two/three"
    "../one/two/three" : "/Users/dhellmann/Documents/PyMOTW/in_progress/one/two/three"

File Times
==========

Besides working with paths, os.path also includes some functions for
retrieving file properties, which can be more convenient than calling
os.stat():

::

    import os.path
    import time

    print 'File         :', __file__
    print 'Access time  :', time.ctime(os.path.getatime(__file__))
    print 'Modified time:', time.ctime(os.path.getmtime(__file__))
    print 'Change time  :', time.ctime(os.path.getctime(__file__))
    print 'Size         :', os.path.getsize(__file__)

::

    $ python ospath_properties.py
    File         : /Users/dhellmann/Documents/PyMOTW/in_progress/ospath/ospath_properties.py
    Access time  : Sun Jan 27 15:40:20 2008
    Modified time: Sun Jan 27 15:39:06 2008
    Change time  : Sun Jan 27 15:39:06 2008
    Size         : 478

Testing Files
=============

When your program encounters a path name, it often needs to know whether the
path refers to a file or directory. If you are working on a platform that
supports it, you may need to know if the path refers to a symbolic link or
mount point. You will also want to test whether the path exists or not.
os.path provides functions to test all of these conditions.

::

    import os.path

    for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
        print 'File        :', file
        print 'Absolute    :', os.path.isabs(file)
        print 'Is File?    :', os.path.isfile(file)
        print 'Is Dir?     :', os.path.isdir(file)
        print 'Is Link?    :', os.path.islink(file)
        print 'Mountpoint? :', os.path.ismount(file)
        print 'Exists?     :', os.path.exists(file)
        print 'Link Exists?:', os.path.lexists(file)
        print

::

    $ ln -s /does/not/exist broken_link
    $ python ospath_tests.py
    File        : /Users/dhellmann/Documents/PyMOTW/in_progress/ospath/ospath_tests.py
    Absolute    : True
    Is File?    : True
    Is Dir?     : False
    Is Link?    : False
    Mountpoint? : False
    Exists?     : True
    Link Exists?: True

    File        : /Users/dhellmann/Documents/PyMOTW/in_progress/ospath
    Absolute    : True
    Is File?    : False
    Is Dir?     : True
    Is Link?    : False
    Mountpoint? : False
    Exists?     : True
    Link Exists?: True

    File        : /
    Absolute    : True
    Is File?    : False
    Is Dir?     : True
    Is Link?    : False
    Mountpoint? : True
    Exists?     : True
    Link Exists?: True

    File        : ./broken_link
    Absolute    : False
    Is File?    : False
    Is Dir?     : False
    Is Link?    : True
    Mountpoint? : False
    Exists?     : False
    Link Exists?: True

Traversing a Directory Tree
===========================

os.path.walk() traverses all of the directories in a tree and calls a function
you provide passing the directory name and the names of the contents of that
directory. This example produces a recursive directory listing, ignoring .svn
directories.

::

    import os.path
    import pprint

    def visit(arg, dirname, names):
        print dirname, arg
        for name in names:
            subname = os.path.join(dirname, name)
            if os.path.isdir(subname):
                print '  %s/' % name
            else:
                print '  %s' % name
        # Do not recurse into .svn directory
        if '.svn' in names:
            names.remove('.svn')
        print

    os.path.walk('..', visit, '(User data)')

::

    $ python ospath_walk.py
    .. (User data)
      .svn/
      ospath/

    ../ospath (User data)
      .svn/
      __init__.py
      ospath_abspath.py
      ospath_basename.py
      ospath_commonprefix.py
      ospath_dirname.py
      ospath_expanduser.py
      ospath_expandvars.py
      ospath_join.py
      ospath_normpath.py
      ospath_properties.py
      ospath_split.py
      ospath_splitext.py
      ospath_tests.py
      ospath_walk.py


