# -*- coding: utf-8 -*-
from zipfile import ZipFile

import pytest
from typer.testing import CliRunner
from yakutils import write_csv

from pyziptar import __version__
from pyziptar.main import app

from .conftest import fake

runner = CliRunner()


@pytest.mark.version
def test_version():
    assert __version__ == "0.0.1"


@pytest.mark.first
def test_app(tmp_path_factory):
    """CSV file and directory creator."""

    mydir = tmp_path_factory.mktemp("mydir")

    a_csv = mydir / "description.csv"

    write_csv(fake(), a_csv)

    a_zip = mydir / "description.zip"

    with ZipFile(a_zip, "w") as f:
        f.write(a_csv)

    result = runner.invoke(app, [a_zip])

    assert result.exit_code == 0
