from src.service.organizer.SpreadSheetOrganizer import SpreadSheetOrganizer

class TestPackOrganize:
    def test_organize_spreadsheet_methods_was_called(self, mocker,tmp_path):
        files = ['report.csv', 'notes.xlsx', 'image.exe']
        organizer = SpreadSheetOrganizer(files, str(tmp_path))
        dir = str(tmp_path) + "/spreadsheets"

        createDirectoryMock = mocker.patch('src.service.organizer.SpreadSheetOrganizer.SpreadSheetOrganizer._createDirectory')
        moveFilesMock = mocker.patch('src.service.organizer.SpreadSheetOrganizer.SpreadSheetOrganizer._moveFilesToDirectory')

        organizer.organize()


        createDirectoryMock.assert_called_once_with(dir)
        moveFilesMock.assert_called_once_with(dir)


    def test_organize_spreadsheet(self, mocker,tmp_path):
        files = ['report.csv', 'notes.xlsx', 'image.exe']
        organizer = SpreadSheetOrganizer(files, str(tmp_path))
        dir = str(tmp_path) + "/spreadsheets"

        createDirMock = mocker.patch('src.service.organizer.SpreadSheetOrganizer.create_dir')
        moveFileMock = mocker.patch('src.service.organizer.SpreadSheetOrganizer.move_file')

        organizer.organize()

        createDirMock.assert_called_once_with(dir)
        moveFileMock.assert_any_call(files[0], dir, overwrite=True)
        assert createDirMock.call_count == 1
        assert moveFileMock.call_count == 2
