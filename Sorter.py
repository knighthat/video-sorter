import os
import re

import PrettierLog as Log
from MediaFile import Media
import shutil


length_pattern = r'^\d{2}\:\d{2}\:\d{2}$'


def sort(media: Media, sort_by: str, option: str, value: str):
    Log.info(f'Sorting: {media.name}')

    if sort_by == 'length':
        sort_this = _sort_by_length(media, option, value)
    elif sort_by == 'size':
        sort_this = _sort_by_size(media, option, value)
    else:
        sort_this = False

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


def _sort_by_length(media: Media, option: str, value: str) -> bool:
    if not re.match(length_pattern, value):
        Log.warn(f'Invalid length! Must be in format ##:##:##')
        Log.warn(f'with "#" is a single digit number')
        return False

    hour, minute, second = value.split(":")
    if int(hour) > 0:
        minute += int(hour) * 60     # Hour to minutes
    if int(minute) > 0:
        second += int(minute) * 60   # Minute to seconds

    result = False
    if option == 'g':
        result = media.length > int(second)
    if option == 'l':
        result = media.length < int(second)
    if option == 'ge':
        result = media.length >= int(second)
    if option == 'le':
        result = media.length <= int(second)

    return result


def _sort_by_size(media: Media, option: str, value: str) -> bool:
    expected = _size_converter(value)
    Log.info(str(expected))
    if expected < 0:
        raise KeyError(f'Size of file cannot be below 0!')

    result = False
    if option == 'g':
        result = media.size > expected
    if option == 'l':
        result = media.size < expected
    if option == 'ge':
        result = media.size >= expected
    if option == 'le':
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
