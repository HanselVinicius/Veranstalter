import typer
from src.service.OrganizeFacade import executeOrganize
app = typer.Typer()

@app.command()
def organize_by_extension(dir:str) -> None:
    executeOrganize(dir)
    