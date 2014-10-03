#!/bin/bash
# pass the settings file to use like this:
#     ./run.sh comedy.settings.production 
#     or
#     ./run.sh comedy.settings.local
set -e

export HOME=/home/redkestrel
export USER=redkestrel

SETTINGS_FILE=$1

LOGFILE=$HOME/logs/gunicorn/comedy.log
PID_FILE=$HOME/projects/comedy/comedy_gunicorn.pid
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=2
# user/group to run as
USER=$USER
GROUP=$USER
SOCKFILE=$HOME/projects/comedy/gunicorn.sock

# go in your project root
cd $HOME/projects/comedy/comedy

# activate the virtualenv
source $HOME/.virtualenvs/comedy/bin/activate

test -d $LOGDIR || mkdir -p $LOGDIR

# --settings=comedy.settings.$SETTINGS_FILE \
exec gunicorn comedy.wsgi:application -w $NUM_WORKERS \
    --log-level=debug \
    --user=$USER \
    --group=$GROUP \
    --bind=unix:$SOCKFILE \
    --pid=$PID_FILE
    --log-file=$LOGFILE 2>>$LOGFILE

