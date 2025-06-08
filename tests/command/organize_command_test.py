from src.command.OrganizeCommand import organize_by_extension

class TestOrganizeCommand:
    def test_organize(self, mocker, tmp_path):
        organize_function_mock = mocker.patch('src.command.OrganizeCommand.executeOrganize')

        organize_by_extension(tmp_path)

        organize_function_mock.assert_called_once_with(tmp_path)
