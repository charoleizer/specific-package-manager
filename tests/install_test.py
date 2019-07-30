from core.install import install
import sys
sys.path.append("..")  # Adds higher directory to python modules path.


def test_all():
    assert install.all() == 'install Class -> all()'