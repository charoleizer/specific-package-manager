from core.init import init
import sys
import json
sys.path.append("..")  # Adds higher directory to python modules path.

def test_full():
    assert init.full('test', 'master') == 'All Done'
    assert json.loads(open('output/packages.json', "r").read()) == {'dependencies': ['https://github.com/charoleizer/specific-package-manager.git: master']}
    assert json.loads(open('output/failed-packages.json', "r").read()) == {'dependencies': []}

def test_simple():
    assert init.simple() == 'init Class -> simple()'
