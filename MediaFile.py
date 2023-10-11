import cv2
import os
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