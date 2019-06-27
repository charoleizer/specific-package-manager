import sys
import collections

from core.init import init
from core.install import install
from core.gc import gc


def main():
    # arg_names is an array with arguments names that will be used to join arguments to his names in args
    arg_names = ['command', 'operation', 'parameter']
    # namedtuple is a tuple that acts like an object, allowing you to access it's values using tuple.attribute.
    # sys.argv is an array that have the arguments passed to main.py.
    # We pass the values from this array, using get to return a default value when the given argument name doesn't have an associated value in the dictionary
    # https://stackoverflow.com/questions/5423381/checking-if-sys-argvx-is-defined
    args = collections.namedtuple('data', arg_names)(*(dict(zip(arg_names, sys.argv[1:])).get(arg, None) for arg in arg_names))
    
    if not(args.command):
        exit()

    if (args.command in ['init']):
        if (args.operation in ['full']):
            if (args.parameter):
                print(init.full(args.parameter))
            else:
                print(init.full())
        else:
            print(init.empty())

    if (args.command in ['install']):
        print(install.all())

    if (args.command in ['gc']):
        print(gc.garbageCollector())

    if (args.command in ['--help', 'help', '-h', '?', '-?']):
        print('Available Commands:')
        print('   init                  Initialize a new empty project')
        print('   init full <Branch>    Initialize a new project with all SysmoS1 projects')
        print('   install               Install all dependency')
        print('   gc                    Garbage Collector')


if __name__ == '__main__':
    main()
