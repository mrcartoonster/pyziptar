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
def test_app(tmp_path):
    """CSV file and directory creator."""

    d = tmp_path / "sub"

    d.mkdir()

    a_csv = d / "description.csv"

    write_csv(fake(), a_csv)

    a_zip = d / "description.zip"

    with ZipFile(a_zip, "w") as f:
        f.write(a_csv)

    result = runner.invoke(app, [a_zip])

    assert a_zip.exists()
    assert result.exit_code == 0


@pytest.mark.second
def test_short_names_option(zipfile_csv):
    """Test that file names are outputted when given -n option."""
    result = runner.invoke(app, [zipfile_csv.name, "-n"])

    assert result.exit_code == 0
    assert "['monopoly.csv']" in result.stdout
