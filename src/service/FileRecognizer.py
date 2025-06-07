from src.model.Extensions import Spreadsheet, Document, Media, Pack
def isSpreadsheet(extension:str) -> bool:
    return extension in Spreadsheet

def isDocument(extension:str) -> bool:
    return extension in Document

def isMedia(extension:str) -> bool:
    return extension in Media

def isPack(extension:str) -> bool:
    return extension in Pack
