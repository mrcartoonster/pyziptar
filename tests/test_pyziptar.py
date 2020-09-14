# -*- coding: utf-8 -*-

import pytest
from typer.testing import CliRunner

from pyziptar import __version__
from pyziptar.main import app

runner = CliRunner()


@pytest.mark.version
def test_version():
    assert __version__ == "0.0.1"


@pytest.mark.first
def test_app(zipfile_csv):
    """CSV file and directory creator."""

    result = runner.invoke(app, [zipfile_csv])

    assert result.exit_code == 0
