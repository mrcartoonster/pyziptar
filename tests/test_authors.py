# -*- coding: utf-8 -*-
import json

import pytest


@pytest.mark.fire
def test_brian_in_portland(author_file_json):
    """A test that uses a data file."""
    with author_file_json.open() as f:
        authors = json.load(f)
    assert authors["Brian"]["City"] == "Portland"


@pytest.mark.smoke
def test_all_have_cities(author_file_json):
    """Same file is used for both tests."""
    with author_file_json.open() as f:
        authors = json.load(f)
    for a in authors:
        assert len(authors[a]["City"]) > 0


@pytest.mark.steam
def test_luciano_in_sao_paulo(author_file_path):
    """A test that uses data file using Path."""
    with author_file_path.open() as f:
        authors = json.load(f)
    assert authors["Luciano"]["City"] == "Sao Paulo"
