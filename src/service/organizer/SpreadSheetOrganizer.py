class SpreadSheetOrganizer:
    def __init__(self, files: list[str]):
        self.files = files

    def organize(self):
        print("Organizing spreadsheet files...")

    def __eq__(self, other):
        if not isinstance(other, SpreadSheetOrganizer):
            return False
        return set(self.files) == set(other.files)

    def __hash__(self):
        return hash(frozenset(self.files))