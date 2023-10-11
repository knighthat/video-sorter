import os

sort_by = [
    'length',
    'size'
]

options = ['g', 'l', 'ge', 'le']


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
                if v[1:] in sort_by:
                    self.sort_by = v[1:]

                    opt = command[i + 1]
                    if opt in options:
                        self.sort_opt = opt
                    else:
                        raise KeyError(f'Unsupported sorting option {opt}')
                else:
                    raise KeyError(f'Unsupported operation {v}')

            if v == command[-1]:
                self.value = v


def validate(cmd : Command) -> list:
    if len(os.listdir(cmd.dir)) == 0:
        return [False, 'Empty directory']

    return [True]
