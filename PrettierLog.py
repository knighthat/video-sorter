#  Copyright (c) 2023. Knight Hat
#  All rights reserved.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights to
#  use,copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#  of the Software, and to permit persons to whom the Software is furnished
#  to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#  WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
#  PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE AUTHORS
#  OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#  OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import logging
import os
from datetime import datetime

workdir = "./logs"
if not os.path.exists(workdir):
    os.makedirs(workdir)

today = datetime.now()
fileName = f'{workdir}/{today.date()}.log'

# Handler for file logging
# File's name follow 'YYYY-MM-DD.log'
fileHandler = logging.FileHandler(fileName)
fileHandler.setLevel(logging.DEBUG)

# Handler for console logging
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

# Apply config
logging.basicConfig(
    format='%(asctime)s [%(threadName)-12.12s / %(levelname)-8.8s] -> %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
    handlers=[fileHandler, consoleHandler]
)
logger = logging.getLogger()
logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)


def deb(s: str):
    logger.debug(s)


def info(s: str):
    logger.info(s)


def warn(s: str):
    logger.warning(s)


def err(s: str):
    logger.error(s)


def crit(s: str):
    logger.critical(s)


def ex(e: Exception):
    logger.exception(msg=e)


def end_of_line():
    with open(fileName, 'a') as log:
        log.write('/-----------------------/\n')
