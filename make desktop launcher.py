#!/usr/bin/env python
import os
import getpass

user = getpass.getuser()
path = os.getcwd()+'/'

def editf():
    a = []
    a.append('[Desktop Entry]')
    a.append('Comment=')
    a.append('Terminal=false')
    a.append('Name=Volum')
    a.append('Exec='+ path + 'Volum.py')
    a.append('Path='+ path)
    a.append('Type=Application')
    a.append('Icon=' + path + 'load/volum.png')
    return a

def savef(text):
    f = open('/home/'+ user + '/Desktop/Volum.desktop', 'w')
    print ('/home/'+ user + '/Desktop/Volum.desktop')
    f.write(text)
    f.close()

def main():
    file = editf()
    text = file = '\n'.join(str(e) for e in file)
    savef(text)
    print('------->')
    print('Done!')


main()
