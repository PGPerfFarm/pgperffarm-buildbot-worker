# -*- python -*-
# ex: set filetype=python:

"""
This is the Buildbot worker configuration file.
"""

import os
import sys

from buildbot_worker.bot import Worker
from twisted.application import service
from twisted.python.logfile import LogFile
from twisted.python.log import ILogObserver, FileLogObserver

try:
    import settings
except Exception as e:
    print("ERROR: local settings.py not found", file=sys.stderr)
    print(e)
    raise

BASEDIR = '.'
ROTATELENGTH = 10000000
MAXROTATEDFILES = 10

# if this is a relocatable tac file, get the directory containing the TAC
if BASEDIR == '.':
    BASEDIR = os.path.abspath(os.path.dirname(__file__))

# note: this line is matched against to check that this is a worker
# directory; do not edit it.
application = service.Application('buildbot-worker')

logfile = LogFile.fromFullPath(
    os.path.join(BASEDIR, "twistd.log"), rotateLength=ROTATELENGTH,
    maxRotatedFiles=MAXROTATEDFILES)
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

BUILDMASTER_HOST = settings.BUILDMASTER_HOST
PORT = 9989
CONNECTION_STRING = None

WORKERNAME = settings.WORKERNAME
PASSWD = settings.PASSWD
KEEPALIVE = 600
UMASK = None
MAXDELAY = 300
NUMCPUS = None
ALLOW_SHUTDOWN = None
MAXRETRIES = None
USE_TLS = 0
DELETE_LEFTOVER_DIRS = 0
PROXY_CONNECTION_STRING = None
PROTOCOL = 'pb'

s = Worker(BUILDMASTER_HOST, PORT, WORKERNAME, PASSWD, BASEDIR,
           KEEPALIVE, umask=UMASK, maxdelay=MAXDELAY,
           numcpus=NUMCPUS, allow_shutdown=ALLOW_SHUTDOWN,
           maxRetries=MAXRETRIES, protocol=PROTOCOL, useTls=USE_TLS,
           delete_leftover_dirs=DELETE_LEFTOVER_DIRS,
           connection_string=CONNECTION_STRING,
           proxy_connection_string=PROXY_CONNECTION_STRING)
s.setServiceParent(application)
