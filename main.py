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

import os
import sys

import Command
import MediaFile as MF
import PrettierLog as Log
import Sorter

# Command template:
# main.py [directory] [sort by] <option> [value]
# - directory: folder contains videos
# - sort by  : length, size
# - option   :
#   g     : greater than
#   l     : less than
#   ge    : greater than or equals to
#   le    : less than or equals to
# - value    : sorting videos based on this


if __name__ == '__main__':
    if len(sys.argv) < 5:
        Log.warn('Not enough argument')
        sys.exit(1)

    try:
        cmd = Command.Command(sys.argv[1:])

        Log.info(f'Dir: {cmd.dir}')
        Log.info(f'Sort By: {cmd.sort_by}')
        Log.info(f'Option: {cmd.sort_opt}')
        Log.info(f'Value: {cmd.value}')

        isValid = Command.validate(cmd)
        if not isValid[0]:
            Log.err(isValid[1])
            sys.exit(1)

        for file in os.listdir(cmd.dir):
            filepath = os.path.join(cmd.dir, file)
            Log.deb(f'Checking file {filepath}')
            if MF.supported(filepath):
                try:
                    media = MF.Media(filepath)
                    media.print()
                    Sorter.sort(media, cmd.sort_by, cmd.sort_opt, cmd.value)
                except OSError:
                    continue

    except Exception as e:
        Log.ex(e)
