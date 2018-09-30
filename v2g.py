#!/usr/bin/env python
import ffmpeg
import argparse
__version__ = '0.0.1'

def options():
    """
    This function parses the options.

    :rtype: class
    :return: argparse.Namespace
    """
    parser = argparse.ArgumentParser(prog='v2g.py',
                                     add_help=True,
                                     description='Tools to convert video to high quality gif using ffmpeg.')

    parser.add_argument('--level', '-l',
                        nargs=1,
                        help='In the case of high image quality, set `high`.')
    parser.add_argument('--yes', '-y',
                        action='store_true',
                        help='Allow overwrite.')
    parser.add_argument('--input', '-i',
                        type=str, required=True,
                        help='Input video file.')
    parser.add_argument('--output', '-o',
                        type=str, default='output.gif',
                        help='Output path and file name.(default: ./output.gif)')
    parser.add_argument('--path', '-p',
                        type=str, default='/tmp',
                        help='Path to save the palette.(default: /tmp)')
    parser.add_argument('--fps', '-f',
                        type=int, default=15,
                        help='Set frame rate.(default: 15)')
    parser.add_argument('--version', '-v',
                        action='version', version='%(prog)s {}'.format(__version__))

    args = parser.parse_args()
    return args

def palettegen(args):
    """
    This function generates a palette image.

    :type args: class
    :param args:

    :rtype: str
    :return: Path that saved palette.png
    """
    stream = ffmpeg.input(args.input)
    stream = ffmpeg.filter(stream, 'palettegen')
    stream = ffmpeg.output(stream, args.path + "/" + "palette.png")
    try:
        ffmpeg.run(stream, overwrite_output=args.yes)
    except Exception as e:
        print("Error: %s" % e)

    return args.path + "/" + "palette.png"

def main():
    args = options()

    if(args.level and args.level[0] == 'high'):
        palette_path = palettegen(args)
        stream = ffmpeg.input(args.input)
        stream = ffmpeg.output(stream, args.output + ".gif", i=palette_path, filter_complex='paletteuse', r=args.fps)
        try:
            ffmpeg.run(stream, overwrite_output=args.yes)
        except Exception as e:
            print("Error: %s" % e)
    else:
        stream = ffmpeg.input(args.input)
        stream = ffmpeg.output(stream, args.output + ".gif", r=args.fps)
        try:
            ffmpeg.run(stream, overwrite_output=args.yes)
        except Exception as e:
            print("Error: %s" % e)

if __name__ == "__main__":
    main()
