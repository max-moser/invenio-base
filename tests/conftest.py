# SPDX-FileCopyrightText: 2015-2018 CERN.
# SPDX-License-Identifier: MIT

"""Pytest configuration."""

import tempfile

import pytest


@pytest.fixture()
def tmppath():
    """Application fixture."""
    tmppath = tempfile.mkdtemp()
    yield tmppath
    return tmppath
