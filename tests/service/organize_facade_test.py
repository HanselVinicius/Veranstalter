from src.service.OrganizeFacade import executeOrganize


class TestOrganizeFacade:

    def test_should_call_get_extensions_and_factory(self, mocker, tmp_path):
        getExtensionsMock = mocker.patch("src.service.OrganizeFacade._getExtensions")
        organizeFactoryMock = mocker.patch("src.service.OrganizeFacade._organizerFactory")

        executeOrganize(tmp_path)

        getExtensionsMock.assert_called_once()
        organizeFactoryMock.assert_called_once()

    
    def test_should_call_organize_for_each_factory(self, mocker, tmp_path):
        files = ['file.txt', 'file.jpg']
        extensions = ['txt', 'jpg']
        
        mocker.patch("src.service.OrganizeFacade._getExtensions",return_value=extensions)

        mocker.patch("src.service.OrganizeFacade.list_files", return_value=files)

        documentOrganizerMock = mocker.Mock()
        mediaOrganizerMock = mocker.Mock()


        mocker.patch("src.service.OrganizeFacade._organizerFactory", return_value={documentOrganizerMock,mediaOrganizerMock})

        executeOrganize(tmp_path)
        documentOrganizerMock.organize.assert_called_once()
        mediaOrganizerMock.organize.assert_called_once()
