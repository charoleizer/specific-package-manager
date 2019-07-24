import sys
import collections

from command.init import initClass
from core.install import install
from core.gc import gc


def main():
    # arg_names is an array with arguments names that will be used to join arguments to his names in args
    arg_names = ['command', 'parameter0', 'parameter1', 'parameter2']
    # namedtuple is a tuple that acts like an object, allowing you to access it's values using tuple.attribute.
    # sys.argv is an array that have the arguments passed to main.py.
    # We pass the values from this array, using get to return a default value when the given argument name doesn't have an associated value in the dictionary
    # https://stackoverflow.com/questions/5423381/checking-if-sys-argvx-is-defined

    args = collections.namedtuple('data', arg_names)(
        *(dict(zip(arg_names, sys.argv[1:])).get(arg, "") for arg in arg_names))

    if not(args.command):
        exit()

    if (args.command in ['init']):
        myInit = initClass(
            args.parameter0, args.parameter1, args.parameter2)
        myInit.doInit()

    if (args.command in ['install']):
        print(install.all())

    if (args.command in ['gc']):
        print(gc.garbageCollector())

    if (args.command in ['--help', 'help', '-h', '?', '-?']):
        print('-------------------')
        print('Available Commands:')
        print('-------------------')
        print(' -  init <Project URL> <Origin>          Initialize a package file with URL Origin or add it to file')
        print('')
        print(' -  init full <Project Name> <Origin>    Initialize a package file with all dependecies of the Project.')
        print('                                         This command  have to be configured in ./configuration/init-full-configurations.ini')
        print('')
        print(' -  install                              Install all dependencies')
        print('')
        print(' -  gc                                   Garbage Collector')
        print('')
        print(' -  config <Path>                        Set configuration file directory')


if __name__ == '__main__':
    main()
