import git
import json
import configparser


# TODO - Transfor in a class and this "constanst" will be setted by cronstructor
# CONFIGFILEDIR will be setted by config commnad
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
    myGitObject = git.cmd.Git()
    # git ls-remote command with url and branch will return a hash if branch exists
    return myGitObject.ls_remote(url, branch).split('\n')[0]



# Exposed methods
def simple():
    return 'init Class -> simple()'



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
