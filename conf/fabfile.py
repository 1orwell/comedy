import datetime

from fabric.api import env, puts, cd
from fabric.contrib.project import rsync_project 
from fabric.colors import _wrap_with  
from fabric.operations import run

env.project = 'comedy'

_green_bg = _wrap_with('42')
_red_bg = _wrap_with('41') 

RSYNC_EXCLUDE = ('.git', 'logs', '*.pyc')

def server():
    # path to the cc directory on the remote server. 
    env.rk_remote_path = '/home/redkestrel/projects/comedy/' 

    # path to the cc directory on the remote server. 
    env.rk_managepy_remote_path = '/home/redkestrel/projects/comedy' 

    # path to the cc directory on the local server. 
    env.rk_local_path = '~/projects/comedy/'

    env.hosts = ['seneca']
    env.user = 'redkestrel'

    env.supervisor_program_name = env.project
    env.supervisorctl = '/usr/bin/supervisorctl' 

    env.virtenv = '/home/redkestrel/.virtualenvs/comedy'

 
def sync():
    """
    Synchronize project with webserver
    """

    puts(_green_bg('Synching comedy'))
    start_time = datetime.datetime.now()

    rsync_project(
                remote_dir=env.rk_remote_path, \
                local_dir=env.rk_local_path, 
                delete=True,
                exclude=RSYNC_EXCLUDE)

    end_time = datetime.datetime.now()
    finish_message = 'Correctly finished synching in %i seconds' % \
        (end_time - start_time).seconds        
    puts(_green_bg(finish_message))

    _collectstatic()
    _supervisor_restart()

def _supervisor_restart():
    res = run("sudo %(supervisorctl)s restart %(supervisor_program_name)s" %
            env, shell=False)
    if 'ERROR' in res:
        print _red_bg("%s NOT STARTED!" % env.supervisor_program_name)
    else:
        print _green_bg("%s correctly started!" % env.supervisor_program_name)


def _collectstatic():
    with cd(env.rk_managepy_remote_path):                                                
        virtenvrun('python manage.py collectstatic')

def virtenvrun(command):
    activate = 'source %s/bin/activate' % env.virtenv
    run(activate + ' && ' + command)


