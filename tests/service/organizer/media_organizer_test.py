from src.service.organizer.MediaOrganizer import MediaOrganizer

class TestMediaOrganize:
    def test_organize_media_methods_was_called(self, mocker,tmp_path):
        files = ['report.jpg', 'notes.txt', 'image.jpg']
        organizer = MediaOrganizer(files, str(tmp_path))
        dir = str(tmp_path) + "/medias"

        createDirectoryMock = mocker.patch('src.service.organizer.MediaOrganizer.MediaOrganizer._createDirectory')
        moveFilesMock = mocker.patch('src.service.organizer.MediaOrganizer.MediaOrganizer._moveFilesToDirectory')

        organizer.organize()


        createDirectoryMock.assert_called_once_with(dir)
        moveFilesMock.assert_called_once_with(dir)


    def test_organize_media(self, mocker,tmp_path):
        files = ['report.jpg', 'notes.txt', 'image.jpg']
        organizer = MediaOrganizer(files, str(tmp_path))
        dir = str(tmp_path) + "/medias"

        createDirMock = mocker.patch('src.service.organizer.MediaOrganizer.create_dir')
        moveFileMock = mocker.patch('src.service.organizer.MediaOrganizer.move_file')

        organizer.organize()

        createDirMock.assert_called_once_with(dir)
        moveFileMock.assert_any_call(files[0], dir, overwrite=True)
        assert createDirMock.call_count == 1
        assert moveFileMock.call_count == 2
