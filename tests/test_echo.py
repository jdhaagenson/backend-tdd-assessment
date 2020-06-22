#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implements a test fixture for the echo.py module

Students are expected to edit this module, to add more tests to run
against the 'echo.py' program.
"""

__author__ = "Jordan Haagenson"

import sys
import importlib
import inspect
import argparse
import unittest
import subprocess
from io import StringIO

# devs: change this to 'soln.echo' to run this suite against the solution
PKG_NAME = 'echo'


# This is a helper class for the main test class
# Students can use this class object in their code
class Capturing(list):
    """Context Mgr helper for capturing stdout from a function call"""
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


# Students can use this function in their code
def run_capture(pyfile, args=()):
    """
    Runs a python program in a separate process,
    returns stdout and stderr outputs as 2-tuple
    """
    cmd = ["python", pyfile]
    cmd.extend(args)
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    stdout, stderr = p.communicate()
    stdout = stdout.decode().splitlines()
    stderr = stderr.decode().splitlines()
    assert stdout or stderr, "The program is not printing any output"
    return stdout, stderr


# Student shall complete this TestEcho class so that all tests run and pass.
class TestEcho(unittest.TestCase):
    """Main test fixture for 'echo' module"""
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested
        cls.module = importlib.import_module(PKG_NAME)
        # Make a dictionary of each function in the student's test module
        cls.funcs = {
            k: v for k, v in inspect.getmembers(
                cls.module, inspect.isfunction
                )
            }
        # check the module for required functions
        assert "main" in cls.funcs, "Missing required function main()"
        assert "create_parser" in cls.funcs, "Missing required function \
                                                create_parser()"

    def setUp(self):
        """Called by parent class ONCE before all tests are run"""
        # your code here - use this space to create any instance variables
        # that will be visible to your other test methods
        pass

    def test_parser(self):
        """Check if create_parser() returns a parser object"""
        result = self.module.create_parser()
        self.assertIsInstance(
            result, argparse.ArgumentParser,
            "create_parser() function is not returning a parser object")

    def test_help(self):
        """Running the program without arguments should show usage"""
        args = ["-h"]
        with open("USAGE") as f:
            usage = f.read().splitlines()
        with Capturing() as output:
            self.module.main(args)
        self.assertEqual(output, usage)

    def test_echo(self):
        """Check if main() function prints anything at all"""
        stdout, stderr = run_capture(self.module.__file__)
        pass

    def test_simple_echo(self):
        """Check if main actually echoes an input string"""
        args = ['Was soll die ganze Aufregung?']
        stdout, stderr = run_capture(self.module.__file__, args)
        self.assertEqual(
            stdout[0], args[0],
            "The program is not performing simple echo"
            )

    def test_lower_short(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["-l", "HELLO WORLD"]
        with Capturing() as output:
            self.module.main(args)
        assert output, "The program did not print anything."
        self.assertEqual(output[0], "hello world")

    def test_lower(self):
        """Checks if '--lower' performs lowercasing"""
        args = ["--lower", "HELLO WORLD"]
        with Capturing() as output:
            self.module.main(args)
        assert output, "The program did not print anything."
        self.assertEqual(output[0], "hello world")

    def test_upper_short(self):
        """Check if short option '-u' performs uppercasing"""
        args = ["-u", "hello world"]
        with Capturing() as output:
            self.module.main(args)
        assert output, "The program did not print anything."
        self.assertEqual(output[0], "HELLO WORLD")

    def test_upper(self):
        """Checks if '--upper' performs uppercasing"""
        args = ["--upper", "hello world"]
        with Capturing() as output:
            self.module.main(args)
        assert output, "The program did not print anything."
        self.assertEqual(output[0], "HELLO WORLD")

    def test_title_short(self):
        """Checks if short option '-t' performs title casing"""
        args = ["-t", "hello world"]
        with Capturing() as output:
            self.module.main(args)
        assert output, "The program did not print anything."
        self.assertEqual(output[0], "Hello World")
    
    def test_title(self):
        """Checks if '--title' performs title casing"""
        args = ["--title", " hello world"]
        with Capturing() as output:
            self.module.main(args)
        assert output, "The program didn't print anything."
        self.assertEqual(output[0], "Hello World")

    def test_all_short(self):
        """Checks when all options are passed"""
        args = ["-ult", "hELlo WoRLd"]
        with Capturing() as output:
            self.module.main(args)
        assert output, "The program did not print anything."
        self.assertEqual(output[0], "Hello World")
    
    def test_noargs(self):
        """Checks that when there are no arguments passed, it just returns unaltered text"""
        args = ["Hello WORLD"]
        with Capturing() as output:
            self.module.main(args)
        assert output, "The program did not print anything"
        self.assertEqual(output[0], "Hello WORLD")
        


if __name__ == '__main__':
    unittest.main()
