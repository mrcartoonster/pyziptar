# -*- coding: utf-8 -*-
from typer.testing import CliRunner

from pyziptar import __version__

runner = CliRunner()


def test_version():
    assert __version__ == "0.1.0"


def test_app():
    pass
