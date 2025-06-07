from fsutil import create_dir,exists,move_file
from src.model.Extensions import Pack
CREATE_DIRECTORY = "packs"

class PackOrganizer:
    def __init__(self, files: list[str], dir: str):
        self.files = [file for file in files if file.endswith(tuple(Pack))]
        print(f"Found {len(self.files)} {CREATE_DIRECTORY} files.")
        self.dir = dir

    def organize(self):
        createDirectory = self.dir + "/" + CREATE_DIRECTORY
        self._createDirectory(createDirectory)
        self._moveFilesToDirectory(createDirectory)

    def _createDirectory(self, dir: str):
        if not exists(dir):
            create_dir(dir) 

    def _moveFilesToDirectory(self, dir: str):
        for file in self.files:
            move_file(file, dir,overwrite=True)

    def __eq__(self, other):
        if not isinstance(other, PackOrganizer):
            return False
        return set(self.files) == set(other.files)

    def __hash__(self):
        return hash(frozenset(self.files))