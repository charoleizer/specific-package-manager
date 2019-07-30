from core.gc import gc
import sys
sys.path.append("..")  # Adds higher directory to python modules path.


def test_garbageCollector():
    if not (gc.garbageCollector() == 'gc class -> garbageCollector()'):
        raise AssertionError()