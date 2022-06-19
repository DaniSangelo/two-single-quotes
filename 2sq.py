import argparse
import re

def main():
    parser = argparse.ArgumentParser(prog="2sq.py")

    parser.add_argument(
        "input", type=str, help="Input File Name"
    )
    parser.add_argument(
        "--output", type=str, help="Output file name"
    )

    args = parser.parse_args()

    with open(args.input, "r") as file:
        filedata = file.read()

    pattern = re.compile(r"R__\S+")
    filename = pattern.findall(args.input)[0]

    filedata = filedata.replace("'", "''")

    with open(f"{filename if args.output is None else args.output}", "w", encoding="cp1252") as file:
        file.write(filedata)

if __name__ == "__main__":
    main()