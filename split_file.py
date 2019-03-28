from tkinter import filedialog
from tkinter import *
from helper import split

def main():
    print('Seleccione un archivo para partir en chunks')
    root = Tk()
    file_to_send = filedialog.askopenfilename()
    root.destroy()

    split_file(file_to_send)

def split_file(path):
    chunk_size = 256*1024
    spl = path.split('/')
    dest = 'split/{}'.format(spl[-1])
    split(path,dest,chunk_size)


if __name__ == '__main__':
    main()