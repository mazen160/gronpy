#!/usr/bin/env python
# coding=utf-8
# *******************************************************************
# *** gron.py ***
# * Description:
# A script that prints JSON objects into "Greppable" output.
# * Homepage:
# https://github.com/mazen160/gronpy
# * Author:
# Mazin Ahmed - <Mazin [at] MazinAhmed [dot] net>
# *******************************************************************

import sys
import json


def traverse(o, previous="", is_finished=False):
    sys.stdout.flush()
    while not is_finished:
        if type(o) == list:
            c = -1
            for i in o:
                c += 1
                current_previous = "[{}]".format(c)
                if type(i) != list and type(i) != dict:
                    x = "{}{}->{}{}".format(previous,
                                            current_previous,
                                            i,
                                            "\n")
                    sys.stdout.write(x)
                else:
                    traverse(i,
                             previous=previous + current_previous,
                             is_finished=False)
        elif type(o) == dict:
            for k in o:
                current_previous = "[{}]".format(k)
                if type(o[k]) != list and type(o[k]) != dict:
                    x = "{}{}->{}{}".format(previous,
                                            current_previous,
                                            o[k],
                                            "\n")
                    sys.stdout.write(x)
                else:
                    traverse(o[k],
                             previous=previous + current_previous,
                             is_finished=False)
        is_finished = True
        sys.stdout.flush()


def main():
    if len(sys.argv) < 2:
        data = sys.stdin.read()
    else:
        data = open(sys.argv[1], "r").read()
    data = json.loads(data)
    traverse(data)
    exit(0)


if __name__ == "__main__":
    main()
