from core.install import install
import sys
sys.path.append("..")  # Adds higher directory to python modules path.


def test_all():
    if not (install.all() == 'install Class -> all()'):
        raise AssertionError()