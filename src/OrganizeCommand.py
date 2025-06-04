import typer

app = typer.Typer()

@app.command()
def organize_by_extension(dir:str):
    print(f"Directory {dir}.")
    