from helper import join

chunk_size = 256*1024
name = 'ubuntu-18.04.2-desktop-amd64.iso'
source = './split/{}'.format(name)
dest = './join/{}'.format(name)

join(source,dest,chunk_size)
