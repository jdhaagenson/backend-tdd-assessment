#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Jordan Haagenson"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="Perform transformation on\
                                                 input text.")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    parser.add_argument("-h" "--help", help="show this message and exit")
    parser.add_argument("-u", "--upper", help='convert text to uppercase')
    parser.add_argument("-l", "--lower", help="convert text to lowercase")
    parser.add_argument("-t", "--title", help="convert text to titlecase")
    parser.add_argument('text', help="text to be manipulated")

    return


if __name__ == '__main__':
    main(sys.argv[1:])
