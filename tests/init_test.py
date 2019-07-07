from core.init import init
import sys
import json
sys.path.append("..")  # Adds higher directory to python modules path.


def test_full():
    assert init.full('test', 'master') == 'All Done'

    assert json.loads(open('output/packages.json', "r").read()) == [
        'https://github.com/charoleizer/specific-package-manager.git: master']

    assert json.loads(open('output/failed-packages.json', "r").read()) == []


def test_empty():
    assert init.empty() == 'init Class -> empty()'
