from src.service.organizer.PackOrganizer import PackOrganizer

class TestPackOrganize:
    def test_organize_pack_methods_was_called(self, mocker,tmp_path):
        files = ['report.rar', 'notes.txt', 'image.exe']
        organizer = PackOrganizer(files, str(tmp_path))
        dir = str(tmp_path) + "/packs"

        createDirectoryMock = mocker.patch('src.service.organizer.PackOrganizer.PackOrganizer._createDirectory')
        moveFilesMock = mocker.patch('src.service.organizer.PackOrganizer.PackOrganizer._moveFilesToDirectory')

        organizer.organize()


        createDirectoryMock.assert_called_once_with(dir)
        moveFilesMock.assert_called_once_with(dir)


    def test_organize_pack(self, mocker,tmp_path):
        files = ['report.rar', 'notes.txt', 'image.exe']
        organizer = PackOrganizer(files, str(tmp_path))
        dir = str(tmp_path) + "/packs"

        createDirMock = mocker.patch('src.service.organizer.PackOrganizer.create_dir')
        moveFileMock = mocker.patch('src.service.organizer.PackOrganizer.move_file')

        organizer.organize()

        createDirMock.assert_called_once_with(dir)
        moveFileMock.assert_any_call(files[0], dir, overwrite=True)
        assert createDirMock.call_count == 1
        assert moveFileMock.call_count == 2
