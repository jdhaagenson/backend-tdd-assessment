#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Jordan Haagenson"


import sys
import argparse


def help():
    with open("USAGE") as f:
        usage = f.read().splitlines()
    print(usage)
    return usage


def upper(text: str):
    return text.upper()


def lower(text: str):
    return text.lower()


def title(text: str):
    return text.title()


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="Perform transformation on\
                                                 input text.")
    parser.add_argument("-u", "--upper", action="store_true", help='convert \
                                                text to uppercase')
    parser.add_argument("-l", "--lower", action="store_true", help="convert \
                                                text to lowercase")
    parser.add_argument("-t", "--title", action="store_true", help="convert \
                                                text to titlecase")
    parser.add_argument('text', default="hElLo WoRlD", help="text to be \
                                                            manipulated")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    result = ns.text

    if ns.title:
        result = title(result)
    elif ns.lower:
        result = lower(result)
    elif ns.upper:
        result = upper(result)
    else:
        result = result

    print(result)
    return(result)


if __name__ == '__main__':
    main(sys.argv[1:])
