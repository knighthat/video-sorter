from enum import Enum


class SupportedFormat(Enum):
    AVI = 'avi'
    MP4 = 'mp4'
    MKV = 'mkv'
    MOV = 'mov'
    FLV = 'flv'


class SortBy(Enum):
    LENGTH = 'length'
    SIZE = 'size'


class SortOption(Enum):
    G = 'g'
    GE = 'ge'
    L = 'l'
    LE = 'le'
