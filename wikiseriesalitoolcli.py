#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: wikiseriesalitoolcli.py
#
# Copyright 2023 asorkun
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#

"""
Main code for wikiseriesalitoolcli.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html

"""

import logging
import logging.config
import json
import argparse
import coloredlogs
import wikiseriesasorkunlib
from wikiseriesasorkunlib.wikiseriesasorkunlib import search_series


__author__ = '''asorkun <alisorkuncuk@gmail.com>'''
__docformat__ = '''google'''
__date__ = '''01-05-2023'''
__copyright__ = '''Copyright 2023, asorkun'''
__credits__ = ["asorkun"]
__license__ = '''MIT'''
__maintainer__ = '''asorkun'''
__email__ = '''<alisorkuncuk@gmail.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".


# This is the main prefix used for logging
LOGGER_BASENAME = '''wikiseriesalitoolcli'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())

def get_arguments():
    """
#    Gets us the cli arguments.#

#    Returns the args as parsed from the argsparser.
#    """
    # https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description='''CLI Tool for trainig''')
    parser.add_argument('--log-config',
                        '-l',
                        action='store',
                        dest='logger_config',
                        help='The location of the logging config json file',
                        default='')
    parser.add_argument('--log-level',
                        '-L',
                        help='Provide the log level. Defaults to info.',
                        dest='log_level',
                        action='store',
                        default='info',
                        choices=['debug',
                                 'info',
                                 'warning',
                                 'error',
                                 'critical'])

    # examples:
    parser.add_argument('--long', '-s',
                        choices=['a', 'b'],
                        dest='parameter_long',
                        action='store',
                        help='Describe the parameter here',
                        default='a',
                        type=str,
                        required=True)

    parser.add_argument('--feature',
                        dest='feature',
                        action='store_true')


    parser.add_argument('--seriesname','-n',
                        action='store',
                        dest='seriesname',
                        help='Name of the series you want to query',
                        type=str,
                        required=True)
    args = parser.parse_args()
    return args


def setup_logging(level, config_file=None):
    """
    Sets up the logging.

    Needs the args to get the log level supplied

    Args:
        level: At which level do we log
        config_file: Configuration to use

    """
    # This will configure the logging, if the user has set a config file.
    # If there's no config file, logging will default to stdout.
    if config_file:
        # Get the config for the logger. Of course this needs exception
        # catching in case the file is not there and everything. Proper IO
        # handling is not shown here.
        try:
            with open(config_file) as conf_file:
                configuration = json.loads(conf_file.read())
                # Configure the logger
                logging.config.dictConfig(configuration)
        except ValueError:
            print(f'File "{config_file}" is not valid json, cannot continue.')
            raise SystemExit(1)
    else:
        coloredlogs.install(level=level.upper())


def main():
    """
    Main method.

    This method holds what you want to execute when
    the script is run on command line.
    """
    args = get_arguments()
    setup_logging(args.log_level, args.logger_config)
    # Search for the movie series on Wikipedia
    search_results = search_series(args.seriesname)
    if not search_results:
        print(f"No results found for '{args.seriesname}'")
        return
        # Choose the first search result

if __name__ == '__main__':
    main()
