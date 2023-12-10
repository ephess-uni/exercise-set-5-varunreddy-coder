"""ex_5_1.py"""
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


import argparse
def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    desc  = "This program prints the number of lines in infile"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('infile',help="provide file path",nargs="?")
    args = parser.parse_args()
    if args.infile:
        main(args.infile)
