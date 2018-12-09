import ctypes
import os
import sys
import random
import numpy as np


def load_lsd_library():

    root_dir = os.path.abspath(os.path.dirname(__file__))
    print(root_dir)

    libnames = ['linux/liblsd.so']
    libdir = 'lib'
    if sys.platform == 'win32':
        if sys.maxsize > 2 ** 32:
            libnames = ['win32/x64/lsd.dll', 'win32/x64/liblsd.dll']
        else:
            libnames = ['win32/x86/lsd.dll', 'win32/x86/liblsd.dll']
    elif sys.platform == 'darwin':
        libnames = ['darwin/liblsd.dylib']
    print(libnames)
    while root_dir != None:
        for libname in libnames:
            try:
                lsdlib = ctypes.cdll[os.path.join(root_dir, libdir, libname)]
                return lsdlib
            except Exception:
                pass
        tmp = os.path.dirname(root_dir)
        if tmp == root_dir:
            root_dir = None
        else:
            root_dir = tmp

    # if we didn't find the library so far, try loading without
    # a full path as a last resort
    for libname in libnames:
        try:
            # print "Trying",libname
            lsdlib = ctypes.cdll[libname]
            return lsdlib
        except:
            pass

    return None
'''
lsdlib = load_lsd_library()
if lsdlib == None:
    raise ImportError('Cannot load dynamic library. Did you compile LSD?')
'''

def lsd(src):
    lsdlib = load_lsd_library()
    if lsdlib == None:
        raise ImportError('Cannot load dynamic library. Did you compile LSD?')
    rows, cols = src.shape
    src = src.reshape(1, rows * cols).tolist()[0]

    temp = os.path.abspath(str(np.random.randint(
        1, 1000000)) + 'ntl.txt').replace('\\', '/')
    print(temp)
    lens = len(src)
    src = (ctypes.c_double * lens)(*src)
    lsdlib.lsdGet(src, ctypes.c_int(rows), ctypes.c_int(cols), temp)

    fp = open(temp[0], 'r')
    cnt = fp.read().strip().split(' ')
    fp.close()
    #os.remove(temp[0])
    count = int(cnt[0])
    dim = int(cnt[1])
    lines = np.array([float(each) for each in cnt[2:]])
    lines = lines.reshape(count, dim)
    return lines
