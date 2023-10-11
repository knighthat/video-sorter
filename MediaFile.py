import cv2
import os
import PrettierLog as Log

supported_formats = [
    'avi',
    'mp4',
    'mkv',
    'mov',
    'flv',
]


def supported(path: str) -> bool:
    if not os.path.exists(path):
        raise FileNotFoundError(f'{path} does not exist!')

    basename = os.path.basename(path)
    filename = basename.split('.')
    return filename[1].lower() in supported_formats


def info(path: str) -> cv2.VideoCapture:
    if not supported(path):
        raise KeyError('Unsupported file')

    video = cv2.VideoCapture(path)

    if not video.isOpened():
        raise IOError(f'Cannot open {path}')

    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    duration = frame_count / fps

    Log.info(f'Video {path} has:')
    Log.info(f'- {frame_count} frames')
    Log.info(f'- width: {frame_width}')
    Log.info(f'- height: {frame_height}')
    Log.info(f'- fps: {fps}')
    Log.info(f'- length: {duration} seconds')

    return video
