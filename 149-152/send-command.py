#!/usr/bin/env python

import sys

if __name__ == '__main__':
    print(sys.argv)     #! sys.argv でcommandline引数のlistが得られる
    print('-' * 20)

    args = sys.argv

    #! listと同じようにアクセスできる
    print("Username: " + args[0])
    print("Password: " + args[1])
    print("Device IP: " + args[2])
    print("Command: " + args[3])