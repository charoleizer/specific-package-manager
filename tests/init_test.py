from core.init import init
import sys
sys.path.append("..")  # Adds higher directory to python modules path.


def test_full():
    assert init.full('test', 'master')[
        0] == 'https://github.com/charoleizer/specific-package-manager.git: master'


def test_empty():
    assert init.empty() == 'init Class -> empty()'
