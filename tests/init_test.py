from core.init import init
import os
import sys
import json
sys.path.append("..")  # Adds higher directory to python modules path.


def test_simple_noFile():
    if (os.path.isfile('output/packages.json')):
        os.remove('output/packages.json')
    
    if not (init.simple('', '') == []):
        raise AssertionError()



def test_simple_invalidFile():
    open('output/packages.json', 'w').write('')
    
    if not (init.simple('', '') == 'There is an invalid file, please remove it: packages.json'):
        raise AssertionError()



def test_full():
    if not (init.full('test', 'master') == 'All Done'):
       raise AssertionError()

    if not (json.loads(open('output/packages.json', "r").read()) == {'dependencies': ['https://github.com/charoleizer/specific-package-manager.git: master']}):
        raise AssertionError()

    if not (json.loads(open('output/failed-packages.json', "r").read()) == {'dependencies': []}):
        raise AssertionError()         

def test_full_noConfig():
    if not (init.full('test_non_exists', 'master') == 'Project test_non_exists cant be found on configuration file'):
        raise AssertionError()



def test_simple_fake():
    if not (init.simple('', '') == {'dependencies': ['https://github.com/charoleizer/specific-package-manager.git: master']}):
        raise AssertionError()



def test_simple():
    if not (init.simple('https://github.com/pytest-dev/pytest.git', 'master') == {'dependencies': ['https://github.com/charoleizer/specific-package-manager.git: master', 'https://github.com/pytest-dev/pytest.git: master']}):
        raise AssertionError() 



def test_full_invalidProject():
    if not (init.full('test', 'Trololo') == 'All Done'):
        raise AssertionError()
    
    if not (json.loads(open('output/failed-packages.json', "r").read()) == {'dependencies': ['https://github.com/charoleizer/specific-package-manager.git: Trololo']}):
        raise AssertionError()