#!/usr/bin/env python3
import sys
import os


def parseCommand(cmd):
    return cmd.split(' ')


def runCommand(cmd):
    """Executes the desired command"""
    os.execvp(cmd[0], cmd)


if __name__ == '__main__':
    promptBegin = os.path.splitext(sys.argv[0])[0]
    while True:
        try:
            print(promptBegin, end="> ")
            runCommand(parseCommand(input()))
        except EOFError as err:
            print()
            exit(0)
