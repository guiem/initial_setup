import pip
from settings import *
try:
    import fabric
except:
    print 'Installing fabric...'
    pip.main(['install','fabric'])
    print 'Fabric installed!'
from fabric.api import *

for server in SERVERS:
    env.host_string = server[0]
    env.user = server[1]
    env.password = server[2]
    env.port = server[3]
    env.warn_only = True
    sudo('apt-get install python-pip')

