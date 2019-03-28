from helper import join

chunk_size = 256*1024
name = 'test.mp4'
source = './split/{}'.format(name)
dest = './join/{}'.format(name)

join(source,dest,chunk_size)
