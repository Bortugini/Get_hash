# _*_ coding: utf-8 _*_

from hashlib import sha256, sha1, md5
from argparse import ArgumentParser, RawDescriptionHelpFormatter, FileType


def get_hash(file, eq_hash, algo, output):
    if algo == "sha256":
        file_hash = sha256()
    if algo == "sha1":
        file_hash = sha1()
    if algo == "md5":
        file_hash = md5()
    # Reads package of 1024 bytes
    with file as file:
        for byte_block in iter(lambda: file.read(1024), b""):
            file_hash.update(byte_block)

        file_hash = file_hash.hexdigest()
        # Check if the hashes are equal
        eq = "False"
        if file_hash == eq_hash:
            eq = "True"

        if output:
            space = len(file_hash) + 3
            print(f"{'Algorithm':9}{' ':3}{'Hash':{space}}{'Hash from':9}{'':3}{'Equal'}")
            print(f"{9 * '='}{' ':3}{(space - 3) * '='}{9 * '=':>12}{'':3}{5 * '='}")
            print(f"{algo:9}{' ':3}{file_hash:{space}}{'File':9}{'':3}{eq:5}")
            print(f"{' ':9}{' ':3}{eq_hash:{space}}{'Input':9}")
        else:
            print(f"{'Equal':5}")
            print(f"{5 * '=':5}")
            print(f"{eq:5}")


def main():
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter, description="""  
                         _____        _     _    _              _     
                        / ____|      | |   | |  | |            | |    
                       | |  __   ___ | |_  | |__| |  __ _  ___ | |__  
                       | | |_ | / _ \| __| |  __  | / _` |/ __|| '_ \ 
                       | |__| ||  __/| |_  | |  | || (_| |\__ \| | | |
                        \_____| \___| \__| |_|  |_| \__,_||___/|_| |_|
    -------------------------------------------------------------------------------------------
    Default hash sha256 without output.
    Options:""")

    # Add options
    parser.add_argument("file", type=FileType("rb"), help="File to check")
    parser.add_argument("eq_hash", type=str, help="Input hash for compare")
    parser.add_argument("-a", "--algorithm", type=str, default="sha256", choices=["sha256", "sha1", "md5"],
                        help="Change algorithm")
    parser.add_argument("-f", "--full", default=False, action="store_true", help="Enable full output")

    args = parser.parse_args()

    get_hash(args.file, args.eq_hash, args.algorithm, args.full)


if __name__ == '__main__':
    main()
