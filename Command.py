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

from Enums import SortBy, SortOption


class Command:
    def __init__(self, command: list[str]) -> None:
        for i, v in enumerate(command):
            if i == 0:
                path = os.path.expanduser(v)
                if path:
                    self.dir = path
                    continue
                else:
                    raise NotADirectoryError(f'{v} is not a directory!')

            if v.startswith('-'):
                self.sort_by = SortBy(v[1:])
                self.sort_opt = SortOption(command[i + 1])

            if v == command[-1]:
                self.value = v


def validate(cmd: Command) -> list:
    if len(os.listdir(cmd.dir)) == 0:
        return [False, 'Empty directory']

    return [True]
