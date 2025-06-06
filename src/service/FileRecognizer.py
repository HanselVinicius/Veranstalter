def isSpreadsheet(extension:str) -> bool:
    return extension in ["csv", "xlsx", "xls"]

def isDocument(extension:str) -> bool:
    return extension in ["doc", "docx", "pdf", "txt", "md", "html"]

def isMedia(extension:str) -> bool:
    return extension in ["jpg", "jpeg", "png", "gif", "mp4", "mp3", "wav", "avi"]

def isPack(extension:str) -> bool:
    return extension in ["zip", "tar", "rar", "7z", "gz","exe"]
