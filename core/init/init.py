import git
import configparser

# Private methods


def isAvailableBranch(url, branch):
    myGitObject = git.cmd.Git()
    # git ls-remote command with url and branch will return a hash if branch exists
    return myGitObject.ls_remote(url, branch).split('\n')[0]

# Exposed methods


def empty():
    return 'init Class -> empty()'


def full(project, origin):
    validProjects = []
    invalidProjects = []
    config = configparser.ConfigParser()
    config.read('configuration/init-full-configurations.ini')

    if (project in config):
        for url in config[project]['DependeciesURL'].split():
            if (isAvailableBranch(url, origin)):
                validProjects.append("".join([url, ': ', origin]))
            else:
                invalidProjects.append("".join([url, ': ', origin]))

        # Build the package file with validProjects and show invalidProjects
        return validProjects
    else:
        return "".join(['Project ', project, ' cant be found on configuration file'])
