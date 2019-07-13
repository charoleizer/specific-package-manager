import os 
import git
import json
import configparser


# TODO - Transfor in a class and this "constanst" will be setted by cronstructor
# Constants 
OUTPUTDIR = 'output/'
PACKAGENAME = 'packages.json'
FAILEDPACKAGENAME = 'failed-packages.json'
CONFIGFILEDIR = 'configuration/init-full-configurations.ini'

# Real Contansts
CONFIGFILE_URL = 'URL'
CONFIGFILE_DependeciesURL = 'DependeciesURL'
DEPENDECY_OBJECT_NAME_JSON = 'dependencies'


# Private methods
def isAvailableBranch(url, branch):
    if not(url) or not(branch):
        return False
    
    myGitObject = git.cmd.Git()
    # git ls-remote command with url and branch will return a hash if branch exists
    return myGitObject.ls_remote(url, branch).split('\n')[0]



# Exposed methods
def simple(url, origin):
    validProjects = []
    # check if is there a verision on packages file, the load it.
    if (os.path.isfile(''.join([OUTPUTDIR, PACKAGENAME]))):
        with open(''.join([OUTPUTDIR, PACKAGENAME])) as f:
            try:
                validProjects = json.load(f)
            except Exception as e:
                print(getattr(e, 'message', repr(e)))
                return "".join(['There is an invalid file, please remove it: ', PACKAGENAME])

    if (isAvailableBranch(url, origin)):
        validProjects[DEPENDECY_OBJECT_NAME_JSON].append("".join([url, ': ', origin]))
    
    return validProjects



def full(project, origin):
    validProjects = []
    invalidProjects = []
    config = configparser.ConfigParser()
    config.read(CONFIGFILEDIR)

    if (project in config):
        for url in config[project][CONFIGFILE_DependeciesURL].split():
            if (isAvailableBranch(url, origin)):
                validProjects.append("".join([url, ': ', origin]))
            else:
                invalidProjects.append("".join([url, ': ', origin]))
    
        with open(''.join([OUTPUTDIR, PACKAGENAME]), 'w') as f:
            f.write(json.dumps({DEPENDECY_OBJECT_NAME_JSON: validProjects}, indent=4))

        with open(''.join([OUTPUTDIR, FAILEDPACKAGENAME]), 'w') as f:
            f.write(json.dumps({DEPENDECY_OBJECT_NAME_JSON: invalidProjects}, indent=4))

        return 'All Done'
    else:
        return "".join(['Project ', project, ' cant be found on configuration file'])
