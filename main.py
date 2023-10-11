import sys
import PrettierLog as Log
import MediaFile as MF
import Command
import os
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

        isValid= Command.validate(cmd)
        if not isValid[0]:
            Log.err(isValid[1])
            sys.exit(1)

        for file in os.listdir(cmd.dir):
            filepath = os.path.join(cmd.dir, file)
            Log.deb(f'Checking file {filepath}')
            if MF.supported(filepath):
                media = MF.Media(filepath)
                media.print()
                Sorter.sort(media, cmd.sort_by, cmd.sort_opt, cmd.value)


        # if not MF.supported(path):
        #     Log.err('Unsupported file')
        #     Log.err(f'Support files: {MF.supported_formats}')
        #     sys.exit(1)
        #
        # video = MF.info(path)

    except Exception as e:
        Log.ex(e)

