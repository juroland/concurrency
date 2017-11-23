''' UNIX system calls '''

import ctypes

SYS_GETTID = 186

LIBC = ctypes.cdll.LoadLibrary(None)


def gettid():
    ''' get thread identification '''
    return LIBC.syscall(SYS_GETTID)
