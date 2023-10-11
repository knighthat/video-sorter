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

import cv2

import PrettierLog as Log
from Enums import SupportedFormat


def supported(path: str) -> bool:
    if not os.path.exists(path):
        raise FileNotFoundError(f'{path} does not exist!')

    if not os.path.isfile(path):
        Log.info(f'{path} is not a file!')
        return False

    basename = os.path.basename(path)
    filename = basename.split('.')
    try:
        SupportedFormat(filename[1].lower())
        return True
    except ValueError:
        return False


class Media:
    def __init__(self, filepath: str) -> None:
        if not supported(filepath):
            raise KeyError('Unsupported file')
        self.name = os.path.basename(filepath)
        self.loc = os.path.dirname(filepath)
        self.path = filepath
        self.size = os.path.getsize(self.path)

        self.video = cv2.VideoCapture(filepath)

        if not self.video.isOpened():
            raise IOError(f'Cannot open {filepath}')

        self.frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        self.length = self.frames / self.fps

    def print(self):
        Log.info(f'Video {self.path} has:')
        Log.info(f'- size: {self.size}')
        Log.info(f'- {self.frames} frames')
        Log.info(f'- width: {self.width}')
        Log.info(f'- height: {self.height}')
        Log.info(f'- fps: {self.fps}')
        Log.info(f'- length: {self.length} seconds')
