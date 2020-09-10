# -*- coding: utf-8 -*-
# from typing import List, Optional
from pathlib import Path
from typing import Optional

# from zipfile import ZipFile
import typer

app = typer.Typer()


@app.command()
def zip(
    path: Optional[Path] = typer.Option(
        Path().cwd(),
        "--path",
        "-p",
        exists=True,
        file_okay=True,
        dir_okay=False,
        resolve_path=True,
        help=(
            (
                "If path is given, zip file extracted in that location."
                "If no path's given, zip file will be extracted in current "
                "working directoy."
            )
        ),
    ),
):
    pass
