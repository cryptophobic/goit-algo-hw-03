import argparse
import re
import shutil
from pathlib import *

class Copy:
    def __init__(self, source, destination):
        self.__source_path = source
        self.__destination_path = destination

    def process(self):
        self.__check_and_prepare()
        self.__recursive_walk(Path(self.__source_path))

    def __check_and_prepare(self):
        source = Path(self.__source_path)
        if not source.exists():
            raise FileNotFoundError(f"{source} does not exist")

        destination = Path(self.__destination_path)
        if not destination.exists():
            destination.mkdir(parents=True, exist_ok=True)

    def __recursive_walk(self, root_path):
        for filename in root_path.iterdir():
            if filename.is_dir():
                self.__recursive_walk(filename)
            else:
                extensions = list(map(lambda suffix: re.sub(r'^\.', '', suffix), PurePath(filename).suffixes))
                directory_path = PurePath(self.__destination_path, *extensions)
                print(directory_path)
                directory = Path(directory_path)
                if not directory.exists():
                    directory.mkdir(parents=True, exist_ok=True)

                if not directory.is_dir():
                    raise NotADirectoryError(f"Directory conflicts with {directory}")

                self.__copy(filename, directory_path, PurePath(filename).name)

    def __copy(self, filename_source, directory_path, filename_dest):
        filename_destination = Path(PurePath(directory_path, filename_dest))
        if filename_destination.exists():
            self.__copy(filename_source, directory_path, f'Copy of {filename_dest}')
        else:
            shutil.copyfile(filename_source, filename_destination)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="Source directory", required=True)
    parser.add_argument("-d", "--destination", help="Destination directory", default='dist')
    args = parser.parse_args()
    copy = Copy(**vars(args))
    copy.process()
