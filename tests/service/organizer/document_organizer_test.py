from src.service.organizer.DocumentOrganizer import DocumentOrganizer

class TestDocumentOrganize:
    def test_organize_documents_methods_was_called(self, mocker,tmp_path):
        files = ['report.pdf', 'notes.txt', 'image.jpg']
        organizer = DocumentOrganizer(files, str(tmp_path))
        dir = str(tmp_path) + "/documents"

        createDirectoryMock = mocker.patch('src.service.organizer.DocumentOrganizer.DocumentOrganizer._createDirectory')
        moveFilesMock = mocker.patch('src.service.organizer.DocumentOrganizer.DocumentOrganizer._moveFilesToDirectory')

        organizer.organize()


        createDirectoryMock.assert_called_once_with(dir)
        moveFilesMock.assert_called_once_with(dir)


    def test_organize_documents(self, mocker,tmp_path):
        files = ['report.pdf', 'notes.txt', 'image.jpg']
        organizer = DocumentOrganizer(files, str(tmp_path))
        dir = str(tmp_path) + "/documents"

        createDirMock = mocker.patch('src.service.organizer.DocumentOrganizer.create_dir')
        moveFileMock = mocker.patch('src.service.organizer.DocumentOrganizer.move_file')

        organizer.organize()

        createDirMock.assert_called_once_with(dir)
        moveFileMock.assert_any_call(files[0], dir, overwrite=True)
        assert createDirMock.call_count == 1
        assert moveFileMock.call_count == 2
