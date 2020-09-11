# -*- coding: utf-8 -*-
# from typing import List, Optional
from pathlib import Path
from typing import Optional

from zipfile import ZipFile
import typer

app = typer.Typer(help="App that unzips zi files given.")


@app.command()
def zip(
    file: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        resolve_path=True,
        help=(
            (
                "File will be extracted in current working directory. To "
                "extract file in selected directory, pass --path/-p flag."
            )
        ),
    ),
    names: Optional[bool] = typer.Option(
        False,
        "--names",
        "-n",
        help="List the file names within the zip file."
    )
):
    if names:
        with ZipFile(file, 'r') as n:
            typer.echo(n.namelist())

    else:
        with ZipFile(file, 'r') as f:
            f.extractall()


if __name__ == "__main__":
    app()
