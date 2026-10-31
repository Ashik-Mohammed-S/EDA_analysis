"""Accept numeric input instead of depending on undefined notebook globals."""
from argparse import ArgumentParser


def total(values):
    return sum(values)


def main():
    parser = ArgumentParser(description="Add the numeric values supplied on the command line.")
    parser.add_argument("values", nargs="*", type=float)
    args = parser.parse_args()
    if args.values:
        print(total(args.values))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

