import git

# Private methods
def isAvailableBranch(url, branch):
    myGitObject = git.cmd.Git() 
    #git ls-remote command with url and branch will return a hash if branch exists   
    return myGitObject.ls_remote(url, branch).split('\n')[0]  

# Exposed methods
def empty():
    return 'init Class -> empty()'

def full(origin = 'develop'):
    if (isAvailableBranch('http://gitlab.sysmo.com.br/dsv-delphi/shared.git', origin)):
        return "".join(['init Class -> full(', origin, ')', ' is available'])
    else:
        return "".join(['init Class -> full(', origin, ')', ' is not available'])
