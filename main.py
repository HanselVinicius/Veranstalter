import typer
import src.OrganizeCommand as OrganizeCommand

app = typer.Typer()

app.add_typer(OrganizeCommand.app, name="organize", help="Organize files in a directory by its extensions.")

if __name__ == "__main__":
    app()