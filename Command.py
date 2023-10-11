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


def validate(cmd : Command) -> list:
    if len(os.listdir(cmd.dir)) == 0:
        return [False, 'Empty directory']

    return [True]
