import subprocess as sp


def run_command(cmdline, **kwargs):
    if not isinstance(cmdline, str):
        cmdline = list(map(str, cmdline))
    sp.check_call(cmdline, **kwargs)


def run_python(args, **kwargs):
    return run_command(["C:\\Python39-x64\\python.exe"] + args, **kwargs)


def python_info():
    run_command(["dir", "C:\\"])
    run_python(['--version'], stderr=sp.STDOUT)
    run_python(
        ['-c', "import sys; print('64bit: %s' % (sys.maxsize > 2**32))"]
    )
