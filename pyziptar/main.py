# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Optional
from zipfile import ZipFile

import typer

app = typer.Typer()


@app.command()
def unzip(
    file: Path = typer.Argument(
        ...,
        metavar="unzipfile",
        exists=True,
        file_okay=True,
        dir_okay=False,
        resolve_path=True,
        help="Pass zipfile(s) to be extracted in current working directory.",
    ),
    names: Optional[bool] = typer.Option(
        False,
        "--names",
        "-n",
        help="List the file names within the zip file.",
    ),
    path: Optional[Path] = typer.Option(
        None,
        "--path",
        "-p",
        exists=False,
        resolve_path=True,
        help="Path zipfile will be extracted to.",
    ),
    pwd: Optional[str] = typer.Option(
        None,
        "--password",
        "-pwd",
        help="Password to unzip password protected zip files.",
    ),
):
    """Unzip zipfiles with all the options!"""
    if names:
        with ZipFile(file, "r") as n:
            typer.echo(n.namelist())

    if path:
        with ZipFile(file, "r") as p:
            p.extractall(path)

    if pwd:
        with ZipFile(file, "r") as pwd:
            p.extractall(path=file, pwd=pwd)

    else:
        with ZipFile(file, "r") as f:
            f.extractall()


if __name__ == "__main__":
    app()
