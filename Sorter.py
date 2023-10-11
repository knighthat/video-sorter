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
import re
import shutil

import PrettierLog as Log
from Enums import SortBy, SortOption
from MediaFile import Media

length_pattern = r'^\d{2}\:\d{2}\:\d{2}$'


def sort(media: Media, sort_by: SortBy, option: SortOption, value: str):
    Log.info(f'Sorting: {media.name}')

    sort_this = False

    if sort_by == SortBy.LENGTH:
        sort_this = _sort_by_length(media, option, value)
    if sort_by == SortBy.SIZE:
        sort_this = _sort_by_size(media, option, value)

    if sort_this:
        _move(media)
    else:
        Log.info(f'Media {media.name} does not meet the requirement\n')


def _move(media: Media):
    sorted_dir = os.path.join(media.loc, 'sorted')
    if not os.path.exists(sorted_dir):
        os.makedirs(sorted_dir)

    t = os.path.join(sorted_dir, media.name)
    shutil.move(media.path, t)

    Log.info(f'Moved {media.name} into {sorted_dir}\n')


def _sort_by_length(media: Media, option: SortOption, value: str) -> bool:
    if not re.match(length_pattern, value):
        Log.warn(f'Invalid length! Must be in format ##:##:##')
        Log.warn(f'with "#" is a single digit number')
        return False

    hour, minute, second = value.split(":")
    if int(hour) > 0:
        minute += int(hour) * 60  # Hour to minutes
    if int(minute) > 0:
        second += int(minute) * 60  # Minute to seconds

    result = False
    if option == SortOption.G:
        result = media.length > int(second)
    if option == SortOption.L:
        result = media.length < int(second)
    if option == SortOption.GE:
        result = media.length >= int(second)
    if option == SortOption.LE:
        result = media.length <= int(second)

    return result


def _sort_by_size(media: Media, option: SortOption, value: str) -> bool:
    expected = _size_converter(value)
    Log.info(str(expected))
    if expected < 0:
        raise KeyError(f'Size of file cannot be below 0!')

    result = False
    if option == SortOption.G:
        result = media.size > expected
    if option == SortOption.L:
        result = media.size < expected
    if option == SortOption.GE:
        result = media.size >= expected
    if option == SortOption.LE:
        result = media.size <= expected

    return result


def _size_converter(value: str) -> int:
    if value.isnumeric():
        return int(value)

    if value.endswith('kb') or value.endswith('KB'):
        return int(value[0:-2]) * 1024

    if value.endswith('mb') or value.endswith('MB'):
        kb = _size_converter(value[0:-2])
        kilobytes = str(kb) + 'kb'
        return _size_converter(kilobytes) * 1024

    if value.endswith('gb') or value.endswith('GB'):
        mb = _size_converter(value[0:-2]) * 1024
        megabytes = str(mb) + 'mb'
        return _size_converter(megabytes) * 1024

    raise KeyError(f'{value} is not a valid size')
