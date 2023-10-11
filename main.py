import sys
import PrettierLog as Log
import MediaFile as MF


if __name__ == '__main__':
    if len(sys.argv) < 2:
        Log.warn('No video provided!')
        sys.exit(1)

    path = sys.argv[1]

    try:
        if not MF.supported(path):
            Log.err('Unsupported file')
            Log.err(f'Support files: {MF.supported_formats}')
            sys.exit(1)

        video = MF.info(path)

    except FileNotFoundError as e:
        Log.ex(e)
