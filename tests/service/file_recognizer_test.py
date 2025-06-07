from src.service.FileRecognizer import isSpreadsheet, isDocument, isMedia, isPack

def test_should_return_true_if_is_spreadSheet():
    result = isSpreadsheet('xlsx')
    assert result is True

def test_should_return_false_if_not_is_spreadSheet():
    result = isSpreadsheet('jpg')
    assert result is False

def test_should_return_true_if_is_document():
    result = isDocument('pdf')
    assert result is True

def test_should_return_false_if_not_is_document():
    result = isDocument('mp4')
    assert result is False

def test_should_return_true_if_is_media():
    result = isMedia('mp4')
    assert result is True

def test_should_return_false_if_not_is_media():
    result = isMedia('zip')
    assert result is False

def test_should_return_true_if_is_pack():
    result = isPack('zip')
    assert result is True

def test_should_return_false_if_not_is_pack():
    result = isPack('docx')
    assert result is False
