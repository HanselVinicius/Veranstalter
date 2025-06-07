from src.service.organizer.PackOrganizer import PackOrganizer
from src.service.organizer.MediaOrganizer import MediaOrganizer
from src.service.organizer.DocumentOrganizer import DocumentOrganizer
from src.service.organizer.SpreadSheetOrganizer import SpreadSheetOrganizer
from fsutil import list_files
from src.service.FileRecognizer import isDocument,isMedia,isPack,isSpreadsheet

def executeOrganize(dir:str) -> None:
    files = list_files(dir)
    extensions = _getExtensions(files) 
    factoryList = _organizerFactory(extensions,files,dir)
    if factoryList is None:
        print("No organizer found for the given extensions.")
        return
    
    for factory in factoryList:
        print(f"factory name :   {factory.__class__.__name__}")
        factory.organize()
    
def _getExtensions(files:list[str]) -> list[str]:
    extensions = set()
    for file in files:
        if '.' in file:
            extension = file.split('.')[-1]
            extensions.add(extension)
    return list(extensions)

def _organizerFactory(extensions:set[str],files:list[str],dir:str) -> set:
    organizers = set()
    for extension in extensions:
        if isSpreadsheet(extension):
            organizers.add(SpreadSheetOrganizer(files,dir))
        elif isDocument(extension):
            organizers.add(DocumentOrganizer(files,dir))
        elif isMedia(extension):
            organizers.add(MediaOrganizer(files,dir))
        elif isPack(extension):
            organizers.add(PackOrganizer(files,dir))
    return organizers